# -*- coding: utf-8 -*-

# Scrapy settings for xpc project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
# 爬虫的名字
BOT_NAME = 'xpc'
# 爬虫所在的模块
SPIDER_MODULES = ['xpc.spiders']
NEWSPIDER_MODULE = 'xpc.spiders'

# http头信息中的user-agent
# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'

# Obey robots.txt rules
# 是否遵循robots协议，如果设置为True，则在爬虫启动时会先抓取网站根目录下的robots.txt文件
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# 并发的请求数量
CONCURRENT_REQUESTS = 4
# 15700156502
# scrapy_redis相关配置
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
REDIS_URL = 'redis://127.0.0.1:6379'
SCHEDULER_PERSIST = True

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
# 配置自定义item pipeline
ITEM_PIPELINES = {
   'xpc.pipelines.MysqlPipeline': 300,
   # 'scrapy_redis.pipelines.RedisPipeline': 301
}

# 每个请求等待的最长时间
DOWNLOAD_TIMEOUT = 10
# 是否启动HTTP 代理
HTTPPROXY_ENABLED = True
# 我们自定义的代理池
PROXIES = [
     'http://211.159.154.164:1703',
     'http://47.100.185.114:1703',
     'http://47.100.173.4:1703',
     'http://47.97.253.250:1703',
     'http://203.195.162.28:1703',
     'http://140.143.143.19:1703',
     'http://106.15.188.107:1703',
     'http://47.100.168.105:1703',
     'http://47.100.176.209:1703',
     'http://47.100.42.205:1703',
     'http://47.100.126.62:1703',
     'http://47.100.169.34:1703',
     'http://101.132.193.81:1703',
     'http://140.143.191.23:1703']

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# 请求之间间隔的时间，单位为秒，也可以设置为小数
# scrapy会自动根据这个值，随机一个具体的数值，作为实际等待时间
# 范围为：0.5 * DOWNLOAD_DELAY 至 1.5 * DOWNLOAD_DELAY
DOWNLOAD_DELAY = 1
# The download delay setting will honor only one of:
# 针对每个域名或者IP并发请求数量
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# 是否使用cookie，如果设置为True，则会启用cookie中间件
COOKIES_ENABLED = True

# Disable Telnet Console (enabled by default)
# 是否启动telnet控制台
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# 默认的请求头信息
# 如果开启了useragent中间件和cookies中间件
# 则headers中的Cookie和User-Agent值会被覆盖
DEFAULT_REQUEST_HEADERS = {
    'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    'Accept-Encoding': "gzip, deflate",
    'Accept-Language': "zh-CN,zh;q=0.9,en;q=0.8",
    'Cache-Control': "no-cache",
    'Connection': "keep-alive",
    'Cookie': "Device_ID=5aa0aa16325fb; _ga=GA1.2.741730614.1521775323; zg_did=%7B%22did%22%3A%20%2216250e0aaadaea-05607d6ea11308-33627805-13c680-16250e0aaaf16c0%22%7D; UM_distinctid=16250e0aac3125-0f3fea18eb61d2-33627805-13c680-16250e0aac48d4; PHPSESSID=l55seqavprk6g86vlmvn73nfb6; Hm_lvt_dfbb354a7c147964edec94b42797c7ac=1525242999,1525314832,1526451149; bdshare_firstime=1526660192587; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216250e0aad08ba-00af24021ca01d-33627805-1296000-16250e0aad1349%22%2C%22%24device_id%22%3A%2216250e0aad08ba-00af24021ca01d-33627805-1296000-16250e0aad1349%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; _gid=GA1.2.66730834.1527730565; Authorization=58E7270F5F0EAEB8D5F0EA4C8A5F0EA98E65F0EA22EEDF63F2D3; ts_uptime=0; zg_c9c6d79f996741ee958c338e28f881d0=%7B%22sid%22%3A%201527730571.123%2C%22updated%22%3A%201527731630.132%2C%22info%22%3A%201527157246741%2C%22cuid%22%3A%2010345093%7D; CNZZDATA1262268826=1769021634-1520317246-%7C1527729099; responseTimeline=110; Hm_lpvt_dfbb354a7c147964edec94b42797c7ac=1527731630; cn_1262268826_dplus=%7B%22distinct_id%22%3A%20%2216250e0aac3125-0f3fea18eb61d2-33627805-13c680-16250e0aac48d4%22%2C%22sp%22%3A%20%7B%22%24_sessionid%22%3A%200%2C%22%24_sessionTime%22%3A%201527731723%2C%22%24dp%22%3A%200%2C%22%24_sessionPVTime%22%3A%201527731723%7D%7D",
    'DNT': "1",
    'Host': "www.xinpianchang.com",
    'Upgrade-Insecure-Requests': "1",
    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",
    }

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
# spider中间件，工作在spider和engine之间
#SPIDER_MIDDLEWARES = {
#    'xpc.middlewares.XpcSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
# 下载器中间件，工作在下载器和engine之间
DOWNLOADER_MIDDLEWARES = {
   # 'xpc.middlewares.RandomProxyMiddleware': 749,
}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
# 插件，根据注册的信号来工作
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}



# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
# 自动控制流量，默认是关闭的
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
# 最开始的时候的下载间隔
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# 最大下载间隔
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# 向同一个服务器同时发送的请求数量
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# 是否打印自动流量控制的相关信息
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# 是否启用HTTP缓存，默认是关闭的
HTTPCACHE_ENABLED = True
# 缓存过期时间，0表示不过期
HTTPCACHE_EXPIRATION_SECS = 0
# 缓存文件的目录
HTTPCACHE_DIR = 'httpcache'
# 忽略哪些HTTP STATUS
HTTPCACHE_IGNORE_HTTP_CODES = []
# 使用何种缓存存储引擎
HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
