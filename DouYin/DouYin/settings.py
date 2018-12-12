# -*- coding: utf-8 -*-

# Scrapy settings for DouYin project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'DouYin'

SPIDER_MODULES = ['DouYin.spiders']
NEWSPIDER_MODULE = 'DouYin.spiders'
"""
http://v3-dy-y.ixigua.com/142d4b8f5187c63b8dfba1a3f6a7eddd/5c106e1f/video/m/2201c3d9450d0074f0883bc8567eec9a06a1161108990000717d7deee444/?rc=amY0M2VzNnFyajMzO2kzM0ApQHRoaGR1KTM8OjU1MzQzMzU0MzQ0NDVvQGgzdSlAZjN1KXB6YnMxaDFwekApNTRkZTNrXjJgY2owXy0tYS0vc3MtbyNqdDppLj8zNC8xMy0uNS02Ly81LTojbyM6YS1xIzpgYmJeZl5fdGJiXmA1Ljo%3D
v0200fd80000bg3omnf3cp5ba0n16chg
"""
VIDEO_FLIE_PATH=r'E:/'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'DouYin (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
'Host':'api.amemv.com',
'Accept':'*/*',
# 'Cookie':'install_id=54011121369; odin_tt=454e44487a676e67673736557a466151b2c1156a24e3bea5ed3e3bb3dfb04d0e9318eeb3f0fe8da9922d4be98a7df0d0; qh[360]=1; ttreq=1$10c0cb9f39511afbbf21cf0852b56f7f902daa90',
'sdk-version':'1',
'User-Agent':'Aweme/3.4.0 (iPhone; iOS 11.2.1; Scale/2.00)',
'Accept-Language':'zh-Hans-CN;q=1',
'Accept-Encoding':'br, gzip, deflate',
'Connection':'keep-alive',

}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'DouYin.middlewares.DouyinSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'DouYin.middlewares.DouyinDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'DouYin.pipelines.DouyinPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
