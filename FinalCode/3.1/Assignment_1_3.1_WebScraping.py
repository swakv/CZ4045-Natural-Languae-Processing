
# SAVING OF THE FILES IS DONE BY MODIFYING SCRAPY FILES - THIS IS JUST CODE FOR SCRAPING
#  
import scrapy
# import Request
from ..items import StackItem

class dataset(scrapy.Spider):
    
    name="dataset"
    start_urls = [
        'https://stackoverflow.com/questions'
    ]
    page = 2
    page_url = 'https://stackoverflow.com/questions?tab=newest&page='
    page_domain = 'https://stackoverflow.com'

    def parse(self, response):
        titles = response.xpath("//a[@class='question-hyperlink']//text()").extract() 
        links = response.xpath("//div[@class='summary']/h3/a[@class='question-hyperlink']/@href").extract()
        content = []
        ques = []
        for link, _ in zip(links, titles):
            request_url = self.page_domain + link
            question = scrapy.http.Request(request_url, callback= self.parse_page, method='GET')
            question = yield question
            try:
                ques.append(question['question'])
                content.append(question['content'])
            except:
                continue

        raw_data = {
            'question': ques,
            'content': content
        }

        yield raw_data

        next_page  = self.page_url +  f'{self.page}'
        self.page+=1
        if self.page <=3:
            yield scrapy.Request(next_page, self.parse)   

    def parse_page(self, response):

        desp_list = response.xpath("//div[@class='post-layout']/div[@class='postcell post-layout--right']/div[@class='s-prose js-post-body']/p//text()").extract()
        # desp = ' '.join(desp_list)
        item = StackItem()
        item['content'] = desp_list
        item['question'] = response.xpath("//a[@class='question-hyperlink']//text()").extract() 
        return item

