import behave
import lxml
import urllib3
import features.configuration

from features.pages.Page import Page
from io import BytesIO
import urllib3
from lxml import etree
from lxml import html
from features.configuration import configuration

class CurrenciesPage(Page):

    def getCurrencyBySymbol(self, context, symbol):
        currency = self.__getTableRowByIndexSymbol__(context, symbol)
        return context.currencies.append(currency)

    def getAllCurrencies(self, context):
        rows = self.__getAllTableRows__(context)
        currency = {}
        for row in rows:
            currency = self.__getRowIndex__(row)
            context.currencies.append(currency)


    def __getRowIndex__(self, row):
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