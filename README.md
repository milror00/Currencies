https://travis-ci.com/milror00/Currencies.svg?branch=master

# Currencies

This is a demo project that uses python - request and behave to scrape the currencies published by yahoo finance. This is a demo to demonstrate the skills I have for scraping. This code is not to be used for any reason commercial or personally other than to demonstrate the approach to scraping.

Requirements to run :

* Python 3.7 above
* requests==2.23.0
* lxml==4.5.0
* urlib3==1.25.9`

Steps for installation:

1. git clone repo
1. pip install -r requirements.txt or poetry install
1. run the yahoo_currencies_scraper.py


Results

|Symbol    |Name                |Last Price     |Change         |%change        |
|----------|-------------------|---------------|---------------|---------------|
|BTCUSD=X  |BTC/USD             |7,693.0620     |+123.1260      |+1.63%         |
|ETHUSD=X  |ETH/USD             |198.7773       |+3.2620        |+1.67%         |
|EURUSD=X  |EUR/USD             |1.0827         |+0.0046        |+0.4223%       |
|JPY=X     |USD/JPY             |107.5200       |-0.1000        |-0.0929%       |
|GBPUSD=X  |GBP/USD             |1.2368         |+0.0021        |+0.1682%       |
|AUDUSD=X  |AUD/USD             |0.6398         |+0.0023        |+0.36%         |
|NZDUSD=X  |NZD/USD             |0.6021         |+0.0010        |+0.17%         |
|EURJPY=X  |EUR/JPY             |116.4100       |+0.4370        |+0.38%         |
|GBPJPY=X  |GBP/JPY             |132.9280       |+0.0840        |+0.06%         |
|EURGBP=X  |EUR/GBP             |0.8753         |+0.0025        |+0.29%         |
|EURCAD=X  |EUR/CAD             |1.5266         |+0.0094        |+0.62%         |
|EURSEK=X  |EUR/SEK             |10.8743        |+0.0237        |+0.22%         |
|EURCHF=X  |EUR/CHF             |1.0530         |+0.0011        |+0.11%         |
|EURHUF=X  |EUR/HUF             |356.3300       |-0.5800        |-0.16%         |
|EURJPY=X  |EUR/JPY             |116.4100       |+0.4370        |+0.38%         |
|CNY=X     |USD/CNY             |7.0812         |+0.0146        |+0.21%         |
|HKD=X     |USD/HKD             |7.7490         |-0.0011        |-0.01%         |
|SGD=X     |USD/SGD             |1.4235         |+0.0005        |+0.03%         |
|INR=X     |USD/INR             |76.2600        |+0.3700        |+0.49%         |
|MXN=X     |USD/MXN             |24.9520        |+0.2030        |+0.82%         |
|PHP=X     |USD/PHP             |50.7500        |+0.1100        |+0.22%         |
|IDR=X     |USD/IDR             |15,550.0000    |-74.0000       |-0.47%         |
|THB=X     |USD/THB             |32.4400        |+0.1150        |+0.36%         |
|MYR=X     |USD/MYR             |4.3570         |+0.0020        |+0.05%         |
|ZAR=X     |USD/ZAR             |19.0211        |-0.0829        |-0.43%         |
|RUB=X     |USD/RUB             |74.4000        |-0.3450        |-0.46%         |
