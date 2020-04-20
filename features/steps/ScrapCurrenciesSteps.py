from behave import given, when, then
from features.configuration.configuration import Configuration
from features.pages.CurrenciesPage import CurrenciesPage


@given(u'I am on the yahoo world indices page')
def step_impl(context):
    config = Configuration()
    page = CurrenciesPage()
    page.getURL(context, config.getBaseURI())

@when(u'I scrape the named currency {text}')
def step_impl(context, text):
    page = CurrenciesPage()
    context.currencies = []
    page.getCurrencyBySymbol(context, text)

@then(u'I output the data to the std out')
def step_impl(context):
    for currency in context.currencies:
        print("Symbol: " + currency['symbol'])
        print("Name: " + currency['name'])
        print("Last Price: " + currency['lastPrice'])
        print("Change: " + currency['change'])
        print("% Change: " + currency['%change'])


@when(u'I scrape all the currencies')
def step_impl(context):
    page = CurrenciesPage()
    context.currencies = []
    page.getAllCurrencies(context)