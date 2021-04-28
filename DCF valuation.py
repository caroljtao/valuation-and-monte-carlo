#Scrape Yahoo Finance
from datetime import datetime
import lxml
from lxml import html
import requests
import numpy as np
import pandas as pd
ticker = 'APPL'
url='https://finance.yahoo.com/quote/'+ ticker +'/balance-sheet?p=' + ticker
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'max-age=0',
    'Pragma': 'no-cache',
    'Referrer': 'https://google.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
}
page = requests.get(url, headers)
tree = html.fromstring(page.content)
tree.xpath("//h1/text()")
