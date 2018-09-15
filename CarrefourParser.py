#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import re
import requests as Request
from urllib import parse
import scrapy
import pymongo
from pymongo import MongoClient

import sys

# https://www.auchandrive.fr/drive/mag/Englos-924
# https://www.auchandrive.fr/recherche/coca

class ProductsSpider(scrapy.Spider):

    # User attributes
    # Store informations
    store_locations = [
        "https://courses-en-ligne.carrefour.fr/set-store/276?sectorZip=59155&sectorCity=Faches-Thumesnil",
    ]
    store_search = [
        "https://courses-en-ligne.carrefour.fr/5449000054227/soda-coca-cola",
        #"https://courses-en-ligne.carrefour.fr/3560070483471",
    ]

    # Class attributes
    name = 'products'
    start_urls = store_locations


    def start_requests(self):
        # Save store location in cookies
        for url in self.start_urls:
            cookiejar = parse.parse_qs(parse.urlparse(url).query)["sectorCity"][0]
            yield scrapy.Request(url, meta={'cookiejar': cookiejar},
                                 dont_filter = True,
                                 callback=self.product_page,
                                 headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"}
                                 )


    def product_page(self, response):
        # Browser product list page
        cookiejar = response.meta["cookiejar"]
        for url in self.store_search:
            # Case single product
            yield scrapy.Request(url,
                                 meta={'cookiejar': cookiejar},
                                 dont_filter = True,
                                 callback=self.parse_product,
                                 headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"}
                                 )


    def parse_product(self, response):
        # Parse product list page
        location = response.meta["cookiejar"]
        save_products = []
        print(response.text)

        SET_SELECTOR = '.cd-ProductPageMainInfos'
        for product in response.css(SET_SELECTOR):
            # Set selector xpath
            PRODUCT_NAME_SELECTOR = './/p[@class="cd-ProductPageTitle cd-span-h1"]/text()'
            PRODUCT_PRICE_SELECTOR = './/p[@class="cd-ProductPriceUnit"]/span/text()'
            PRODUCT_PRICEPER_SELECTOR = './/p[@class="cd-ProductPriceReference"]/text()'

			# Process data
            product_name = re.sub(r"(\n *)", "", product.xpath(PRODUCT_NAME_SELECTOR).extract_first())
            product_price = "".join(product.xpath(PRODUCT_PRICE_SELECTOR).extract()).replace("\u20ac", "")
            product_priceper = re.sub(r" \u20ac.*", "", product.xpath(PRODUCT_PRICEPER_SELECTOR).extract_first())

            # Format data
            mongo_data = {
                'Date': datetime.datetime.now(),
                'Company': 'Carrefour',
                'Location': location,
                'Product': product_name,
                'Price': product_price,
                'Priceper': product_priceper,
            }

            self.save_mongo(mongo_data)
        

    def save_mongo(self, product_data):
        # Save products in Mondo Database
        # Here is a dev/test database
        #client = MongoClient("ds141872.mlab.com", 41872)
        client = MongoClient("localhost", 27017)
        db = client['auchan-products']
        db.authenticate("scrapy59", "scrapy59")
        collection = db['products']

        collection.insert(product_data)