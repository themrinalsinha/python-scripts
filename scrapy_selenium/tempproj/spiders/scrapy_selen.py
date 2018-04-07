from scrapy   import Spider, Request
from selenium import webdriver
from scrapy.selector import Selector
from selenium.common.exceptions import NoSuchElementException

from time import sleep

class SeleniumScrapy(Spider):
    name = 'scrapy_selen'

    def start_requests(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://books.toscrape.com/index.html')
        source = Selector(text = self.driver.page_source)
        book_links = source.xpath('//li/article/h3/a/@href').extract()
        for book_url in book_links:
            yield Request('http://books.toscrape.com/' + book_url, callback = self.temptest)

        while True:
            try:
                next_page = self.driver.find_element_by_xpath('//a[text()="next"]')
                sleep(5)
                next_page.click()
            except NoSuchElementException:
                self.driver.quit()
                break

    def temptest(self, response):
        print('In temptest')
        pass