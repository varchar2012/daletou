# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DaletouItem(scrapy.Item):
    issue = scrapy.Field()
    q_one = scrapy.Field()
    q_two = scrapy.Field()
    q_three = scrapy.Field()
    q_four = scrapy.Field()
    q_five = scrapy.Field()
    h_one = scrapy.Field()
    h_two = scrapy.Field()
    first_num = scrapy.Field()
    first_money = scrapy.Field()
    first_addnum = scrapy.Field()
    firat_addmoney = scrapy.Field()
    second_num = scrapy.Field()
    second_monkey = scrapy.Field()
    second_addnum = scrapy.Field()
    second_addmoney = scrapy.Field()
    sales = scrapy.Field()
    prize_pool = scrapy.Field()
    open_date = scrapy.Field()
