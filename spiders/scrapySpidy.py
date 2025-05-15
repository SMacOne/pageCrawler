import scrapy
from urllib.parse import urlparse


# import re

class ScrapyspidySpider(scrapy.Spider):
    name = "scrapySpidy"
    page_limit = 6  # Limita a 10 pagine
    pages_visited = 0
    elenco_domini = set()
    sito = ""

    # allowed_domains = ["example.com"]

    def start_requests(self):
        with open('esempio.txt', 'r') as f:
            self.start_urls = f.read().splitlines()
        for url in self.start_urls:
            self.elenco_domini.add(urlparse(url).netloc)
        for url in self.start_urls:
            self.pages_visited = 0
            # allowed_domains = urlparse(url).netloc
            # self.logger.debug(f'AllOWED DOMAIN************************************: {allowed_domains}')
            yield scrapy.Request(
                url,
                meta=dict(
                    playwright=True,  # Abilita Playwright per questa richiesta
                    playwright_page_methods=[  # Specifica le azioni di Playwright
                        {
                            "method": "wait_for_selector",
                            "args": ["div.quote"]
                        }
                    ],
                )
            )
        pass

    def parse(self, response):
        page_title = response.css('title::text').get()
        text_elements = response.css('h1::text, h2::text, p::text').getall()
        url_name = response.url

        if self.pages_visited == 0 and urlparse(url_name).netloc in self.elenco_domini:
            self.sito = url_name
            self.logger.debug(f'NOME URL************************************: {url_name}')
            yield {
                "Prima pagina del Sito": url_name,
                "Page Title": page_title,
                "Text Elements": text_elements,
            }
            links = response.xpath('//a/@href').getall()  # Usa XPath per ottenere l'attributo href di tutti i tag <a>
            for link in links:
                # Gestisci link assoluti e relativi
                if self.pages_visited < self.page_limit:
                    self.pages_visited += 1
                    absolute_url = response.urljoin(link)
                    self.logger.debug(f'Link Numero: {self.pages_visited}')
                    self.logger.debug(f'Found link: {absolute_url}')
                    # self.log(f'Link Numero: {self.pages_visited}')
                    # self.log(f'Found link: {absolute_url}')
                    yield scrapy.Request(absolute_url, callback=self.parse)
                else:
                    self.pages_visited = 0
                    self.sito = ""
                    break
        else:
            if urlparse(url_name).netloc in self.elenco_domini:
                yield {
                    "Indirizzo del Sito": self.sito,
                    "url Link": url_name,
                    "Numero del Link": self.pages_visited,
                    "Page Title": page_title,
                    "Text Elements": text_elements,
                }
        pass
