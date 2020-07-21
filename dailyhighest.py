from yahoo_fin import stock_info as si
import pprint as pp
from random import randint
stocklist = ["WEGE3","ITSA4","ABCB4"]
exchange = []
class Stock:
    def __init__(self, ticker_, min_, max_, now_):
        self.ticker_ = ticker_
        self.min_ = min_
        self.max_ = max_
        self.now_ = now_


for item in stocklist:
   exchange.append(Stock(item,randint(0, 100),randint(0, 100),randint(0, 100)))


for item in exchange:
    print(item.ticker_,item.min_) 
