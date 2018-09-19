import scrapy
from daletou.items import DaletouItem
class DltSpider(scrapy.Spider):
    name = 'dlt_spider'
    allowed_domains = ['www.lottery.gov.cn']
    start_urls = ['http://www.lottery.gov.cn/historykj/history.jspx?_ltype=dlt']

    def parse(self,response):
        nums =  response.xpath("//tbody/tr")
        for num in nums:
            dlt_item = DaletouItem()
            dlt_item['issue'] = num.xpath("./td[1]/text()").extract()
            dlt_item['q_one'] = num.xpath("./td[2]/text()").extract()
            dlt_item['q_two'] = num.xpath("./td[3]/text()").extract()
            dlt_item['q_three'] = num.xpath("./td[4]/text()").extract()
            dlt_item['q_four'] = num.xpath("./td[5]/text()").extract()
            dlt_item['q_five'] = num.xpath("./td[6]/text()").extract()
            dlt_item['h_one'] = num.xpath("./td[7]/text()").extract()
            dlt_item['h_two'] = num.xpath("./td[8]/text()").extract()
            dlt_item['first_num'] = num.xpath("./td[9]/text()").extract()
            dlt_item['first_money'] = num.xpath("./td[10]/text()").extract()
            dlt_item['first_addnum'] = num.xpath("./td[11]/text()").extract()
            dlt_item['firat_addmoney'] = num.xpath("./td[12]/text()").extract()
            dlt_item['second_num'] = num.xpath("./td[13]/text()").extract()
            dlt_item['second_monkey'] = num.xpath("./td[14]/text()").extract()
            dlt_item['second_addnum'] = num.xpath("./td[15]/text()").extract()
            dlt_item['second_addmoney'] = num.xpath("./td[16]/text()").extract()
            dlt_item['sales'] = num.xpath("./td[18]/text()").extract()
            dlt_item['prize_pool'] = num.xpath("./td[19]/text()").extract()
            dlt_item['open_date'] = num.xpath("./td[20]/text()").extract()

            # print(dlt_item)
            yield dlt_item 
        next_link = response.xpath("//div[@class='page']/div/a[3]/@href").extract()
        print(next_link)
        print(next_link[0])
        if next_link:
            next_link = next_link[0]
            yield scrapy.Request("http://www.lottery.gov.cn/historykj/"+next_link,callback=self.parse)    