This is a beta version.
It will not work withouth a proper Proxy configuration 

To install software use following steps
1.	Download project in a local directory(Download Zip project end extrat files in a local Directory)
2.	With an IDE like Pycharm, open from menu bar( New File --- New Project) set the local directory in project directory field and open project.
3.	Open the IDE Terminal.
   
5.	If u don't see a virtual environment in the project before to continue create it first!
6.	
7.	Navigate in the directory tree until to reach the project directory (pageCrawlyPrj)
8.	To reach the project directory in the terminal use these commands (Cd..  cd pageCrawlyPrj)
9.	Install project dependencies (pip install  -r requirements.txt --proxy http://proxy.istat.it:8080). If u don't have a proxy delete  --proxy http://proxy.istat.it:8080 from the command line
10.	Run the spider (scrapy crawl newSpider)

Istructions to run project without a proxy

