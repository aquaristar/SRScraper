# -*- coding: utf-8 -*-
import scrapy


class ConseilSpider(scrapy.Spider):
    name = "conseil"
    allowed_domains = ["conseil-national.medicin.fr"]
    start_urls = (
        'http://www.conseil-national.medicin.fr/',
    )

    def parse(self, response):
        pass
