import pandas as pd
import pandas_datareader.data as web
import yfinance as yf

yf.pdr_override()  #这一行代码非常重要

all_data = {ticker: web.get_data_yahoo(ticker)
            for ticker in ['AAPL', 'IBM', 'MSFT', 'GOOG']}

price = pd.DataFrame({ticker: data['Adj Close']
                     for ticker, data in all_data.items()})
volume = pd.DataFrame({ticker: data['Volume']
                      for ticker, data in all_data.items()})

returns = price.pct_change()
print(returns.tail())