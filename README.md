This is a beta version.
It will not work withouth a proper Proxy configuration 

To install software use following steps
1.	Download project in a local directory(Download Zip project end extrat files in a local Directory)
2.	With an IDE like Pycharm, open from menu bar( New File --- New Project) set the local directory in project directory field and open project.
3.	Open the IDE Terminal.
   
4.	If u don't see a virtual environment in the project before to continue create it first! PyCharm usually create a virtual environment each time u open a new project.
  
5.	Navigate in the directory tree until to reach the project directory (pageCrawlyPrj)
6.	To reach the project directory in the terminal use these commands (Cd..  cd pageCrawlyPrj)
7.	Install project dependencies (pip install  -r requirements.txt --proxy http://proxy.istat.it:8080). If u don't have a proxy delete  --proxy http://proxy.istat.it:8080 from the command line
8.	Run the spider (scrapy crawl newSpider)



*********************************************************************
Istructions to run project without a proxy


inside the settings.py files delete:

PLAYWRIGHT_BROWSER_TYPE = "chromium"
PLAYWRIGHT_LAUNCH_OPTIONS = {
    "headless": True,
    "proxy": {"server": "http://proxy.istat.it:8080"}
}

DOWNLOADER_MIDDLEWARES = {
    'pageCrawlyPrj.middlewares.CustomProxyMiddleware': 350,
}

*********************************************************************

inside the file middelwares.py file delete:

class CustomProxyMiddleware(object):
    def __init__(self):
        self.proxy = 'http://proxy.istat.it:8080'

    def process_request(self, request, spider):
        if 'proxy' not in request.meta:
            request.meta['proxy'] = self.proxy

    def get_proxy(self):
        return self.proxy


