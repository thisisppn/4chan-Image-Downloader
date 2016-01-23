import scrapy
import FourChan.items as items

class imageSpider(scrapy.Spider):
    name = "imageSpider"
    allowed_domains = ["4chan.org"]
    thread = raw_input("Enter thread link: ")
    start_urls = [
        thread
        # "http://boards.4chan.org/a/thread/136492097/would-you-still-stay-with-you-waifu-if-she-was",
    ]


    def parse(self, response):
        page = response
        item = items.FourchanItem()
        testCss = page.selector.css('.fileThumb::attr(href)').extract()
        for test in testCss:
            url = "http:"+test
            # url = test[2:]
            filename = url.split("/")[-1]
            # print filename
            item['fileName'] = filename
            item['image_urls'] = [url] #This needs to be a list, in order for the image pipeline to work, can't be a string
            yield item