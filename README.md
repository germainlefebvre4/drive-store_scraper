# Drive Store Scraper

**Summary**
1. [Global Application](#global-application)
   1. [The Workflow](#the-workflow)
1. [Zoom on the Sraper](#zoom-on-the-scraper)
   1. [The incomings](#the-outcomings)
   1. [The outcomings](#the outcomings)
1. [Dependencies](#context-and-dependencies)
1. [Run the app](#running-the-scrap)


## Global application

### The Workflow

This application is part of a fullchain applications having the goal of providing the best product price from all drive stores registered.

Global application schema :
```
                                                             Customer  
                                                                 |     
                                                                 |     
+-------------+      +--------------+      +---------+      +---------+
|   Scraper   |------|   Database   |------|   Api   |------|   Gui   |
+------+------+      +--------------+      +---------+      +---------+
       |                                                               
       |                                                               
  Drive Stores                                                         
+----+                                                                 
|   +----+                                                             
+---|   +----+                                                         
    +---|    |                                                         
        +----+                                                         
```

Quick description of each step :
* Scraper : Catches product prices,
* Database : Stores product prices,
* Api : Provides REST Api to process/read Product Prices,
* Gui : Offers a interface to interact with the Api.


## Zoom on the Scraper

The aim of the scraper is to periodically retrieve the products informations from drive stores and to store them in the database.

The Scraper will reach and parse the products pages to retrieve prices, product price and product per unit price in order to correlate data to reveal the best amount for the registered cart.

Products prices are stored as documents in a NoSQL Database, here MongoDB, to keep a trace of prices. This will allow to see the trend of product prices and predict them.


## Dependencies

Code run from Visual Studio Code 2017 with Python and C++ environements configured. Python version selected is python-3.6 because of dependencies with scrapy package (not compatible with python-3.7 yet).

Required python libs :
* `pywin32` (Visual Studio)
* `requests`
* `scrapy`
* `pymongo`


## Run the app

Quickstart application
```shell
scrapy runspider PriceScraper.py
```
