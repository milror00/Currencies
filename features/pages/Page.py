import lxml
import requests
import urllib3
from io import BytesIO
from lxml import etree
from lxml import html

from features.configuration.configuration import Configuration


class Page:

    def getURL(self, context,  url):
        http = urllib3.PoolManager()
        config = Configuration()
        context.response = http.request('GET',config.getBaseURI())

    def __getTableRowByIndexSymbol__(self, context, symbol):
        rows = self.__getAllTableRows__(context)
        currency = {}
        for row in rows:
            currency = self.__getRowIndex__(row)
            if (currency['symbol'] == symbol):
                return currency
        return currency

    def __getAllTableRows__(self, context):
        dom = lxml.html.parse(BytesIO(context.response.data))
        # all table rows
        xpatheval = etree.XPathDocumentEvaluator(dom)
        rows = xpatheval('//table/tbody/tr')
        return rows

