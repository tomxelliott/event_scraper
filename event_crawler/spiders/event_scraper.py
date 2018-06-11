import csv
import json
import sys

from scrapy.http import Request as request
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import HtmlXPathSelector
from event_crawler.items import EventItem

def parse_input():
    while True:
        try:
            no_of_pages = int(raw_input("How many pages of results would you like? \n"))
            if no_of_pages <= 0:
                raise ValueError
        except ValueError:
            print "Please enter a positive number."
        except KeyboardInterrupt:
            sys.exit()
        else:
            break
    return no_of_pages


class EventSpider(CrawlSpider):
    name = "events"
    allowed_domains = ["wegottickets.com"]
    start_urls = ["http://www.wegottickets.com/searchresults/adv"]

    no_of_pages = parse_input()

    for page in range(1, no_of_pages):
        start_urls.append('http://www.wegottickets.com/searchresults/page/' + str(page) + '/adv#paginate')

    def parse(self, response):
        for event in response.xpath('//div[contains(@class, "content block-group chatterbox-margin")]'):
            item = EventItem()
            item["artist"] = event.xpath('.//a[@class="event_link"]/text()').extract()
            item["venue"] = event.xpath('.//div[@class="venue-details"]/h4[1]/text()').extract()
            item["date"] = event.xpath('.//div[@class="venue-details"]/h4[2]/text()').extract()
            item["price"] = event.xpath('.//div[@class="searchResultsPrice"]/strong/text()').extract()
            yield item