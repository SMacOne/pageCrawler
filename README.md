This is a beta version.
Check the network proxy settings before to use it!

To install software use following steps
1.	Download project in a local directory(Download Zip project end extract files in a local Directory)
2.	With an IDE, like Pycharm, open from menu bar( New File --- New Project) and set in the window as field "local directory", the directory previously chosen fo unzipping the project.
3. in the field "project name", insert the name of the project "pageCrawlyPrj"
4. complete the creation of the project, the sistem will ask you if u desire recharge data from existing project, confirm yes.
5. Open the IDE Terminal.
   
6.	If you aren't using a virtual environment, before to continue let create it! PyCharm usually create a virtual environment, each time, on new project creation (venv).

7. To create a virtual environment in your IDE: Execute the follow command: python -m venv name_environment, name_environment is the name of tne new virtual environment (any name you want). 


   Activate the virtual Environment:

   On Windows: name_environment\Scripts\activate.
   
   On macOS and Linux: name_environment/bin/activate.
  
8.	Navigate inside the directory tree until to reach the top project directory (pageCrawlyPrj)
9.	To reach the project directory inside the terminal use the command (cd..)
10.	Install project dependencies (pip install  -r requirements.txt --proxy http://proxy.istat.it:8080). If u aren't behind a proxy, delete "--proxy http://proxy.istat.it:8080" from the command line
11.	Run the spider (scrapy crawl newSpider)

*********************************************************************
Problems with playwryght component
solution: reinstall playwright with the following command: playwright install

In the case u get the following error message:
****
      Downloading Chromium 128.0.6613.18 (playwright build v1129) from https://playwright-verizon.azureedge.net/builds/chromium/1129/chromium-win64.zip
      Error: connect ETIMEDOUT 13.107.246.60:443
          at TCPConnectWrap.afterConnect [as oncomplete] (node:net:1607:16) {
        errno: -4039,
        code: 'ETIMEDOUT',
        syscall: 'connect',
        address: '13.107.246.60',
        port: 443
      }
      Failed to install browsers
      Error: Failed to download Chromium 128.0.6613.18 (playwright build v1129), caused by
      Error: Download failure, code=1
****


download playwright manually at the following link: https://playwright-verizon.azureedge.net/builds/chromium/1129/chromium-win64.zip


extract everything in the following directory : ..\AppData\Local\ms-playwright\chromium-1129\chrome-win
if the path doesn't exist, create it manually.
At the end of extraction process, verify if the "chrome-win" directory contains the file "chromium.exe" 



If something go wrong and you need to restart the scrapy project, in the terminal reach the higher level (pageCrawlyPrj) directory and type the following command: scrapy startproject pageCrawlyPrj

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


inside the file middelwares.py file delete:

      class CustomProxyMiddleware(object):
          def __init__(self):
              self.proxy = 'http://proxy.istat.it:8080'
      
          def process_request(self, request, spider):
              if 'proxy' not in request.meta:
                  request.meta['proxy'] = self.proxy
      
          def get_proxy(self):
              return self.proxy


