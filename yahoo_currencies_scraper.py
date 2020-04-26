import lxml
import requests
import urllib3
from io import BytesIO
from lxml import etree
from lxml import html



"""
Class description:
Get financial currency data from Yahoo finance and save it to db.

Author:
	Rob Milroy
	
Website:
	https://pyscrape.com
	
Modify:
	2020-04-26
"""
class YahooCurrencies():

    def __init__(self):
        self.url = 'https://finance.yahoo.com/currencies'
        self.headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.8',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.109 Safari/537.36'}

    def getURL(self):
        try:
            http = urllib3.PoolManager()
            self.response = http.request('GET', self.url)
        except Exception as e:
            print(e)
            exit(1)

    def getAllTableRows(self):
        dom = lxml.html.parse(BytesIO(self.response.data))
        # all table rows
        xpatheval = etree.XPathDocumentEvaluator(dom)
        rows = xpatheval('//table/tbody/tr')
        return rows

    def getRowIndex(self, row):
        currency = {}
        columns0 = row.findall("td/a")
        columns1 = row.findall("td")
        columns2 = row.findall("td/span")
        currency['symbol'] = columns0[0].text
        currency['name'] = columns1[1].text
        currency['lastPrice'] = columns1[2].text
        currency['change'] = columns2[0].text
        currency['%change'] = columns2[1].text
        return currency


    def getAllCurrencies(self):
        self.getURL()
        rows = self.getAllTableRows()
        results = []
        currency = {}
        for row in rows:
            currency = self.getRowIndex(row)
            results.append(currency)
        return results

if __name__ == '__main__':
    currencies = YahooCurrencies()
    results = currencies.getAllCurrencies()
    #headers
    print('|{0: <10}|{1: <20}|{2: <15}|{3: <15}|{4: <15}|'.format(
        'Symbol',
        'Name',
        'Last Price',
        'Change',
        '%change'))
    print('|----------|-------------------|---------------|---------------|---------------|')
    #data
    for currency in results:
        print('|{0: <10}|{1: <20}|{2: <15}|{3: <15}|{4: <15}|'.format(
            currency['symbol'],
            currency['name'],
            currency['lastPrice'],
            currency['change'],
            currency['%change'],
        ))

