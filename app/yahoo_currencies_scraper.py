import requests
import lxml
from bs4 import BeautifulSoup

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

    def getURL(self):
        try:
            request = requests.get(url=self.url)
            request.encoding = 'utf-8'
            html = request.text
            self.page_bf = BeautifulSoup(html, 'lxml')
        except Exception as e:
            print(e)
            exit(1)

    def getAllTableRows(self):
        # all table rows
        tables = self.page_bf.findChildren('table')
        rows = tables[0].findChildren(['th', 'tr'])
        return rows

    def getAllCurrencies(self):
        self.getURL()
        rows = self.getAllTableRows()
        results = []
        for row in rows:
            cells = row.findChildren('td')
            currency = {}
            for cell in cells:
                currency['symbol'] = cells[0].string
                currency['name'] = cells[1].string
                currency['lastPrice'] = cells[2].string
                currency['change'] = cells[3].string
                currency['%change'] = cells[4].string
                results.append(currency)
                break
        return results


if __name__ == '__main__':
    currencies = YahooCurrencies()
    results = currencies.getAllCurrencies()
    # headers
    print('|{0: <10}|{1: <20}|{2: <15}|{3: <15}|{4: <15}|'.format(
        'Symbol',
        'Name',
        'Last Price',
        'Change',
        '%change'))
    print('|----------|-------------------|---------------|---------------' +
          '|---------------|')
    # data
    for currency in results:
        print('|{0: <10}|{1: <20}|{2: <15}|{3: <15}|{4: <15}|'.format(
            currency['symbol'],
            currency['name'],
            currency['lastPrice'],
            currency['change'],
            currency['%change'],
        ))
