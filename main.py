import investpy
from tradingview_ta import TA_Handler, Interval, Exchange
import pandas as pd
import pandas_ta as ta
import numpy as np
from pandas_datareader import data as pdr
from ta import add_all_ta_features
from ta.utils import dropna
from ta.volatility import BollingerBands
import yfinance as yf
from datetime import date



def print_info():
  today = date.today()
  print("Šodienas datums:","[",today,"]")
  txt = ('\033[94m{}\033[0m'.format("[ZPD tehniskā analīze]"))
  INF = txt.center(65)
  print(INF)

  
def fromcsv():
  print("Enter stock ticker")
  ticker = input()
  print("Enter 1 - Starting Ear, 2 - starting Mounths, 3 - starting date ")
  SE = input()
  SM = input()
  SD = input()
  print("Enter 1 - end Ear, 2 - end Mounths, 3 - end date ")
  EE = input()
  EM = input()
  ED = input()

  a = SE+"-"+SM+"-"+SD
  #print(a)
  b = EE+"-"+EM+"-"+ED
  #print(b)

  #yf.pdr_override()

  #data = yf.download(ticker, start=a, end=b,group_by="ticker")

  #data = pdr.get_data_yahoo(ticker, start=a, end=b)
  #np.savetxt('AAPL.csv', data, delimiter=',')
  df = pd.read_csv('AAPL.csv', sep=',')
  df = dropna(df)
  df = add_all_ta_features(
  df, open="Open", high="High", low="Low", close="Close", volume="Volume", fillna=True)
  print(df)
  print(df.columns.tolist())
  df_complete = df.dropna()
  df = dropna(df)
  array = np.array(df_complete)
  np.savetxt('AAPL_v2.csv', array, delimiter=',')


def instant():
  ticker = input()
  
  t_sum = TA_Handler(
      symbol=ticker,
      screener="america",
      exchange="NASDAQ",
      interval=Interval.INTERVAL_1_DAY,
  )
  print(t_sum.get_analysis().summary)
  
  data = investpy.moving_averages(name=ticker,     country='United States', product_type='stock', interval='daily')
  
  print(data.head())
  
  data_1 = investpy.technical_indicators(name=ticker, country='United States', product_type='stock', interval='daily')
  
  print(data_1.head())




def test():
  #a = input()
  #b = input()
  #c = a+"-"+a+"-"+b
  #print(c)
  ticker = yf.Ticker("TSLA")
  df = ticker.history(period="1y")
  print(df.info)


def alreadyDownloadet():
  name = input()
  df = pd.read_csv(name+".csv", sep=',')
  df.replace("?" , "Unknow" , inplace = True)
  df_complete = df.dropna()
  df = dropna(df)
  array = np.array(df_complete)
  df = add_all_ta_features(
  df, open="Open", high="High", low="Low", close="Close", volume="Volume", fillna=True)
  #print(df.info)
  indicator_bb = BollingerBands(close=df["Close"], window=20, window_dev=2)
  #df['bb_bbm'] = indicator_bb.bollinger_mavg()
  #df['bb_bbh'] = indicator_bb.bollinger_hband()
  #df['bb_bbl'] = indicator_bb.bollinger_lband()
  #df['bb_bbhi'] = indicator_bb.bollinger_hband_indicator()
  #df['bb_bbli'] = indicator_bb.bollinger_lband_indicator()
  print(indicator_bb)
  print(df)
  print(array)

def fromExperement():
  print("aa")







def directCSV():
  print("brrr")
  ticker = yf.Ticker("TSLA")
  df = ticker.history(period="1y")
  adx = ta.adx(df['high'], df['low'], df['close'])
  adx = df.ta.adx()
  df = pd.DataFrame(columns=['time', 'open', 'high', 'low', 'close', 'volume'])
  print(df)
  macd = df.ta.macd(fast=14, slow=28)
  rsi = df.ta.rsi()
  df = pd.concat([df, adx, macd, rsi], axis=1)
  df = df[df['RSI_14'] < 30]
  macd = df.ta.macd(fast=14, slow=28)
  print(macd)

  

print_info()
print("Izvēlieties veidu")
choose = input()
if choose == '1':
  instant()
if choose == '2':
  fromcsv()
if choose == 't':
  test()
if choose == '3':
  alreadyDownloadet()
if choose == '4':
  fromExperement()
if choose == '5':
  directCSV()
else:
  exit
