# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import Join, MapCompose
from w3lib.html import replace_escape_chars


class AusEventsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Date = scrapy.Field(input_processor=MapCompose(lambda v: v.split(),replace_escape_chars,unicode.strip),output_processor=Join(),)
    Name = scrapy.Field(input_processor=MapCompose(lambda v: v.split(),replace_escape_chars,unicode.strip),output_processor=Join(),)
    Organizer = scrapy.Field(input_processor=MapCompose(lambda v: v.split(),replace_escape_chars,unicode.strip),output_processor=Join(),)
    Location = scrapy.Field(input_processor=MapCompose(lambda v: v.split(),replace_escape_chars,unicode.strip),output_processor=Join(),)
    pass
