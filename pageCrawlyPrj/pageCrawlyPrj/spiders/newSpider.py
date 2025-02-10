import scrapy
import csv
from scrapy.crawler import CrawlerProcess
from urllib.parse import urlparse


class NewspiderSpider(scrapy.Spider):
    name = "newSpider"
    # page_limit = 10  # Limita a 10 pagine
    elenco_domini = set()
    dic_asia_code = {}
    dic_elenco_domini = {}

    # creare un vocabolario vuoto pet tutti i codici asia
    def start_requests(self):
        # with open('istat_elenco.txt', 'r') as f:
        #     self.start_urls = f.read().splitlines()

        # with open('istat_seeds.txt', mode='r', newline='') as file:
        with open('C:/Users/stefano.macone/PycharmProjects/pageCrawler/pageCrawlyPrj/istat_seeds.txt', mode='r',
                  newline='') as file:
            # Creare un oggetto CSV DictReader
            csv_reader = csv.DictReader(file, delimiter='\t')

            # Iterare sulle righe del file CSV
            # for row in csv_reader:
            #     print(row)
            # for url in self.start_urls:
            #     self.elenco_domini.add(urlparse(url).netloc)
            for row in csv_reader:
                # allowed_domains = urlparse(url).netloc
                # self.logger.debug(f'AllOWED DOMAIN************************************: {allowed_domains}')

                # aggiungere il codice asia al vocabolario e settare il valore a zero

                self.logger.debug(f'RICHIESTA PAGINA DEL SITO************************************: {row["url"]}')
                self.logger.info(f'RICHIESTA PAGINA DEL SITO************************************: {row["url"]}')
                self.elenco_domini.add(urlparse(row['url']).netloc)
                self.dic_asia_code[row['cod_asia']] = 0
                self.dic_elenco_domini[urlparse(row['url']).netloc] = 0
                yield scrapy.Request(
                    row['url'],

                    meta= dict(

                        playwright=True,  # Abilita Playwright per questa richiesta
                        playwright_page_methods=[  # Specifica le azioni di Playwright
                            {
                                "method": "wait_for_selector",
                                "args": ["div.quote"]
                            }
                        ],
                        # playwright_context_kwargs={
                        #     "proxy": {
                        #         "server": " http://proxy.istat.it:8080"
                        #     }
                        # },
                        cod_asia=row['cod_asia']
                    )
                )

    def parse(self, response):
        page_title = response.css('title::text').get()
        text_elements = response.css('h1::text, h2::text, p::text').getall()
        url_name = response.url
        cod_asia = response.meta.get('cod_asia')
        self.dic_elenco_domini[urlparse(url_name).netloc] += 1
        if urlparse(url_name).netloc in self.elenco_domini and self.dic_asia_code[cod_asia] < 6:

            self.dic_asia_code[cod_asia] += 1
            yield {
                "firm_id": cod_asia,
                "url": url_name,
                "title": page_title,
                "page_body": text_elements[0],
            }
            # links = response.xpath('//a/@href').getall()  # Usa XPath per ottenere l'attributo href di tutti i tag <a>

            links = response.xpath('//a[not(ancestor::a)]/@href').getall()
            for link in links:
                # Gestisci link assoluti e relativi
                absolute_url = response.urljoin(link)
                self.logger.debug(f'Found link: {absolute_url}')
                # self.logger.debug(f'Dizionario Asia: {self.dic_asia_code}')
                # self.logger.debug(f'Dizionario Domini: {self.dic_elenco_domini}')
                self.logger.info(f'Found link: {absolute_url}')
                # self.logger.info(f'Dizionario Asia: {self.dic_asia_code}')
                # self.logger.info(f'Dizionario Domini: {self.dic_elenco_domini}')
                # self.dic_elenco_domini[urlparse(absolute_url).netloc] < 20
                if urlparse(absolute_url).netloc in self.elenco_domini:
                    # yield response.follow(absolute_url, callback=self.parse_link)
                    yield scrapy.Request(url=absolute_url, callback=self.parse, meta={"cod_asia": cod_asia})
                    # yield scrapy.Request(
                    #     absolute_url,
                    #     meta=dict(
                    #         playwright=True,  # Abilita Playwright per questa richiesta
                    #         playwright_page_methods=[  # Specifica le azioni di Playwright
                    #             {
                    #                 "method": "wait_for_selector",
                    #                 "args": ["div.quote"]
                    #             }
                    #         ],
                    #         cod_asia=cod_asia
                    #     )
                    # )

    def parse_link(self, response):
        # Estrai ulteriori dettagli dal link
        # if urlparse(response.url).netloc in self.elenco_domini:
        self.logger.debug(f'Trovato Link: {response.url}')
        title = response.css('title::text').get()
        textelements = response.css('h1::text, h2::text, p::text').getall()
        yield {
            "url Link": response.url,
            # "Numero del Link": self.pages_visited,
            "Page Title": title,
            "Text Elements": textelements,
        }


# process=CrawlerProcess()
# process.crawl(NewspiderSpider)
# process.start()
