Thia project to to download the data from yahoo/quandl, 
and then save it to self-customized db securities_masters

1. The download job is trying to construct the following request to yahoo
https://query1.finance.yahoo.com/v7/finance/download/AAPL?period1=1531107604&period2=1533786004&interval=1d&events=history&crumb=cx8/honqAZu
https://query1.finance.yahoo.com/v7/finance/download/SYMBOL?period1=tuple1&period2=tuple2&interval=1d&events=history&crumb=cx8/honqAZu

2. In case of fobbiden call, fix yahoo download as below
```buildoutcfg
from __future__ import print_function
import datetime
import fix_yahoo_finance as yf

if __name__ == "__main__":
    spy = yf.download(
        "SPY",
        datetime.datetime(2000, 1, 1).strftime("%Y-%m-%d"),
        datetime.datetime(2015, 6, 15).strftime("%Y-%m-%d")
    )
    print(spy.tail())
```
   
3. some sql cmd for reference
```buildoutcfg
mysql -usec_user -p
password
use securities_master
select count(*) from daily_price 



SELECT *
FROM symbol AS sym
INNER JOIN daily_price AS dp
ON dp.symbol_id = sym.id
WHERE sym.ticker = 'TSLA'
ORDER BY dp.price_date ASC
limit 10;

``` 
