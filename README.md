# Drive Store Scraper

**Summary**
1. [Global View](#global-view)
   1. [Global application](#global-application)
   1. [Workflow](#workflow)
1. [Zoom on the Sraper](#zoom-on-the-scraper)
   1. [General](#general)
   1. [Configuration](#configuration)
1. [Dependencies](#dependencies)
1. [Run the app](#run-the-app)
   1. [Quickstart](#quickstart)
1. [Production eligibility](#production-eligibility)


## Global View

### Global application

This application is part of a fullchain applications which have the goal to provide the best product prices from all drive stores for a registered cart.

### Workflow

To provide a structured data requestable application a chain of steps is required. This chain catch the raw data and store it in a structured way. This data is thus queryable and optimized for processing.

You can find a quick sight of the Data Journey below.

**Global application schema**
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

### General

The aim of the scraper is to periodically retrieve the products informations from drive stores and to store them in the database.

The Scraper will reach and parse the products pages to retrieve prices, product price and product per unit price in order to correlate data to reveal the best amount for the registered cart.

Products prices are stored as documents in a NoSQL Database, here MongoDB, to keep a trace of prices. This will allow to see the trend of product prices and predict them.

### Configuration

All the application configuration is stored in the `conf/` directory.


## Dependencies

Code run from Visual Studio Code 2017 with Python and C++ environements configured. Python version selected is python-3.6 because of dependencies with scrapy package (not compatible with python-3.7 yet).

Required python libs :
* `pywin32` (Visual Studio)
* `requests`
* `scrapy`
* `pymongo`


## Run the app

### Quickstart

```shell
scrapy runspider PriceScraper.py
```

## Production eligibility
