# -*- coding: utf-8 -*-
import json
import scrapy
from scrapy import Request
from scrapy_redis.spiders import RedisSpider
from xpc.items import PostItem, CopyrightItem, CommentItem, ComposerItem


class DiscoverySpider(RedisSpider):
    name = 'discovery'
    allowed_domains = ['xinpianchang.com']
    # start_urls = ['http://www.xinpianchang.com/channel/index/type-0/sort-like/duration_type-0/resolution_type-/page-2396']

    # def start_requests(self):
    #     for url in self.start_urls:
    #         request = Request(url, dont_filter=True)
    #         request.meta['dont_merge_cookies'] = True
    #         yield request

    def make_requests_from_url(self, url):
        """ This method is deprecated. """
        request = Request(url, dont_filter=True)
        request.meta['dont_merge_cookies'] = True
        return request

    def parse(self, response):
        post_url = 'http://www.xinpianchang.com/a%s?from=ArticleList'
        post_list = response.xpath('//ul[@class="video-list"]/li')
        for post in post_list:
            pid = post.xpath('./@data-articleid').get()
            request = Request(post_url % pid, callback=self.parse_post)
            request.meta['pid'] = pid
            request.meta['thumbnail'] = post.xpath('./a/img/@_src').get()
            request.meta['duration'] = post.xpath(
                './/span[contains(@class, "duration")]/text()').get()
            request.meta['dont_merge_cookies'] = True
            yield request
        next_page = response.xpath('//a[@title="下一页"]/@href').get()
        if next_page:
            request = Request(next_page, callback=self.parse)
            request.meta['dont_merge_cookies'] = True
            yield request


    def parse_post(self, response):
        post = PostItem()
        pid = response.meta['pid']
        post['pid'] = pid
        post['thumbnail'] = response.meta['thumbnail']
        minutes, seconds, *_ = response.meta['duration'].split("'")
        post['duration'] = int(minutes) * 60 + int(seconds)
        post['video'] = response.xpath('//video[@id="xpc_video"]/@src').get()
        post['preview'] = response.xpath(
            '//div[@class="filmplay"]//img/@src').extract_first()
        post['title'] = response.xpath('//div[@class="title-wrap"]/h3/text()').get()
        cates = response.xpath('//span[contains(@class, "cate")]/a/text()').extract()
        post['category'] = '-'.join([strip(cate) for cate in cates])
        post['created_at'] = response.xpath(
            '//span[contains(@class, "update-time")]/i/text()').get()
        post['play_counts'] = response.xpath(
            '//i[contains(@class, "play-counts")]/@data-curplaycounts').get()
        post['like_counts'] = response.xpath(
            '//span[contains(@class, "like-counts")]/@data-counts').get()
        post['description'] = strip(response.xpath(
            '//p[contains(@class, "desc")]/text()').get())
        yield post

        creator_list = response.xpath(
            '//div[contains(@class, "filmplay-creator")]/ul/li')
        url = 'http://www.xinpianchang.com/u%s?from=articleList'
        for creator in creator_list:
            cid = creator.xpath('./a/@data-userid').get()
            # url = 'http://www.xinpianchang.com%s' % creator.xpath('./a/@href').get()
            request = Request(url % cid, callback=self.parse_composer)
            request.meta['cid'] = cid
            yield request
            cr = CopyrightItem()
            cr['pcid'] = '%s_%s' % (cid, pid)
            cr['cid'] = cid
            cr['pid'] = pid
            cr['roles'] = creator.xpath(
                './/span[contains(@class, "roles")]/text()').get()
            yield cr
        comment_url = 'http://www.xinpianchang.com/article/filmplay/ts-getCommentApi?id=%s&ajax=0&page=1'
        request = Request(comment_url % pid, callback=self.parse_comment)
        request.meta['pid'] = pid
        yield request

    def parse_comment(self, response):
        result = json.loads(response.text)
        comments = result['data']['list']
        for c in comments:
            comment = CommentItem()
            comment['commentid'] = c['commentid']
            comment['pid'] = response.meta['pid']
            comment['cid'] = c['userInfo']['userid']
            comment['uname'] = c['userInfo']['username']
            comment['avatar'] = c['userInfo']['face']
            comment['created_at'] = c['addtime']
            comment['content'] = c['content']
            comment['like_counts'] = c['count_approve']
            if c['reply']:
                comment['reply'] = c['reply']['commentid']
            yield comment
        next_page = result['data']['next_page_url']
        if next_page:
            request = Request(next_page, callback=self.parse_comment)
            request.meta['pid'] = response.meta['pid']
            yield request

    def parse_composer(self, response):
        composer = ComposerItem()
        composer['cid'] = response.meta['cid']
        # 背景大图
        composer['banner'] = response.xpath(
            '//div[@class="banner-wrap"]/@style').get()[21:-1]
        # 用户头像
        composer['avatar'] = response.xpath(
            '//span[@class="avator-wrap-s"]/img/@src').get()
        composer['name'] = response.xpath(
            '//p[contains(@class, "creator-name")]/text()').get()
        composer['intro'] = response.xpath(
            '//p[contains(@class, "creator-desc")]/text()').get()
        # 人气
        composer['like_counts'] = clean(response.xpath(
            '//span[contains(@class, "like-counts")]/text()').get())
        # 粉丝数量
        composer['fans_counts'] = clean(response.xpath(
            '//span[contains(@class, "fans-counts")]/text()').get())
        # 关注数量
        composer['follow_counts'] = clean(response.xpath(
            '//span[@class="follow-wrap"]/span[2]/text()').get())
        # 位置
        composer['location'] = response.xpath(
            '//span[contains(@class, "icon-location")]'
            '/following-sibling::span[1]/text()').get()
        # 职业
        composer['career'] = response.xpath(
            '//span[contains(@class, "icon-career")]'
            '/following-sibling::span[1]/text()').get()
        yield composer


def strip(s):
    if s:
        return s.strip()


def clean(number):
    if number:
        return number.replace(',', '')
    else:
        return ''

