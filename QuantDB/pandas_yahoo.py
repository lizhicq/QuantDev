from __future__ import print_function
import fix_yahoo_finance as yf

if __name__ == "__main__":
    spy = yf.download(
        "ZION",
        "2000-01-01",
        "2018-08-08"
    )
    print(spy.tail())