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