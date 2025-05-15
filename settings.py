# Scrapy settings for pageCrawlyPrj project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "pageCrawlyPrj"

SPIDER_MODULES = ["pageCrawlyPrj.spiders"]
NEWSPIDER_MODULE = "pageCrawlyPrj.spiders"

DUPEFILTER_CLASS = "scrapy.dupefilters.RFPDupeFilter"  # Attivo di default
# SCHEDULER_PRIORITY_QUEUE = 'scrapy.pqueues.DownloaderLifoPriorityQueue'  # Depth-First
DEPTH_LIMIT = 3  # Numero massimo di livelli da esplorare
DEPTH_PRIORITY = 0  # Preferisci andare più in profondità prima di esplorare altre pagine
# DOWNLOAD_DELAY = 1
# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = "pageCrawlyPrj (+http://www.yourdomain.com)"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False
CONCURRENT_REQUESTS_PER_DOMAIN = 5  # Limita a 5 richieste per dominio
CONCURRENT_REQUESTS = 30  # Limita il numero totale di richieste parallele
# CLOSESPIDER_PAGECOUNT = 10

#HTTP_PROXY = "http://proxy.istat.it:8080"



PLAYWRIGHT_BROWSER_TYPE = "chromium"
PLAYWRIGHT_LAUNCH_OPTIONS = {
    "headless": True,
    "proxy": {"server": "http://proxy.istat.it:8080"}
}
DOWNLOADER_MIDDLEWARES = {
    'pageCrawlyPrj.middlewares.CustomProxyMiddleware': 350,
}
# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#    "Accept-Language": "en",
# }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    "pageCrawlyPrj.middlewares.PagecrawlyprjSpiderMiddleware": 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    "pageCrawlyPrj.middlewares.PagecrawlyprjDownloaderMiddleware": 543,
# }

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    "pageCrawlyPrj.pipelines.PagecrawlyprjPipeline": 300,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = "httpcache"
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"

# Imposta Playwright come downloader
DOWNLOAD_HANDLERS = {
    "http": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
    "https": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
}

# Disabilita il middleware di download predefinito per i timeout di Scrapy (facoltativo)
DOWNLOAD_HANDLERS_BASE = {
    "http": None,
    "https": None,
}

# Impostazioni Playwright (numero di browser contemporanei)

FEEDS = {
    'output5.json': {
        'format': 'json',
        'encoding': 'utf8',
        'store_empty': False,  # Non salvare item vuoti
        'indent': 4,  # Indentazione per il file JSON
        'fields': None,  # Se vuoi specificare un ordine dei campi, puoi indicarlo qui
        'overwrite': False,  # Sovrascrivi il file se esiste già
    },
}
LOG_LEVEL = 'INFO'
PLAYWRIGHT_LOG_LEVEL = "info"
LOG_FILE = 'scrapy_log.txt'
