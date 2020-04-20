# Created by Oem at 19/04/2020
Feature: To scrape the currencies from the yahoo finance page

  Scenario Outline: scrape a named currency

  Given I am on the yahoo world indices page
  When I scrape the named currency <name>
  Then I output the data to the std out

  Examples:
    |name       |
    |BTCUSD=X   |


  Scenario: scrape all currencies

  Given I am on the yahoo world indices page
  When I scrape all the currencies
  Then I output the data to the std out

