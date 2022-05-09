# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import sqlite3

conn = sqlite3.connect('db.sqlite3')
from finta import TA
import yfinance as yf
import requests
import time
import pandas as pd
import numpy as np
import datetime as dt
import json
import math
# from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
from finta import TA
import yfinance as yf
import requests
import time
import pandas as pd
import numpy as np
import datetime as dt
import json
# from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager

from datetime import date

import pandas as pd
import time
import sys

# local modules
from binance.client import Client
from binance.enums import *
# from indicator import indicators

# local file
import secrets

import yfinance as yf
import numpy as np
import datetime as dt
import requests 
import json 
import pandas as pd 
import numpy as np  
import requests
import time
import urllib


# %%
symbol='BTCUSDT'
take_profit=2
stop_loss=1
time_frame='15m'
percentage=10


# %%
conn = sqlite3.connect('db.sqlite3')
c= conn.cursor()

c.execute("SELECT * FROM shop_bot1")

data1=c.fetchall()
conn.commit()

conn.close()


# %%
data1[1][0]


# %%

def candle_initial(symbol, interval):
    global j,Low_main,High_main,position

    root_url = 'https://api.binance.com/api/v1/klines'
    url = root_url + '?symbol=' + symbol + '&interval=' + interval
    data = json.loads(requests.get(url).text)
    df = pd.DataFrame(data)
    df.columns = ['Datetime',
                'Open', 'High', 'Low', 'Close', 'volume',
                'close_time', 'qav', 'num_trades',
                'taker_base_vol', 'taker_quote_vol', 'ignore']
    df.index = [dt.datetime.fromtimestamp(x / 1000.0) for x in df.close_time]
    
    df.drop(['close_time','qav','num_trades','taker_base_vol', 'taker_quote_vol', 'ignore'],axis=1,inplace=True)
    
    
    df['Open']=pd.to_numeric(df["Open"], downcast="float")
    df["High"]=pd.to_numeric(df["High"], downcast="float")
    df["Low"]=pd.to_numeric(df["Low"], downcast="float")
    df["Close"]=pd.to_numeric(df["Close"], downcast="float")
    df["volume"]=pd.to_numeric(df["volume"], downcast="float")
    df['SMA 21']=TA.SMA(df,21)
    df['SMA 10']=TA.SMA(df,10)

    return df


# %%
def ltp_price(instrument,client):
    prices = client.get_all_tickers()
    for i in range(len(prices)):
        if prices[i]['symbol']==str(instrument):
            
            return float(prices[i]['price'])


# %%
def market_order(instrument):

    try:
        global quantity,data1

        ltp=ltp_price(instrument)
        for i in range(len(data1)):
            client=Client(data1[i][4],data1[i][5])
            data=client.futures_account_balance()
            percentage=data[i][3]
            for j in range(len(data)):
                
                if data[j]['asset']=='USDT':
                    p_l=float(data[j]['withdrawAvailable'])   
            quantity=(((float(percentage))/100) * p_l)/ltp
            quantity=quantity*1
            quantity=quantity*1000


            quantity=math.floor(quantity)

            quantity=quantity/1000
            quantity1[str(data1[i][0])]=quantity




            try:
                order = client.futures_create_order(
                    symbol=str(instrument),
                    side=Client.SIDE_BUY,
                    type=Client.ORDER_TYPE_MARKET,
                
                    
                    quantity=round(quantity,3))
            except Exception as e:
                # bot.sendMessage(1190128536,str(e))
                pass


    except Exception as e:
        print(str(e))
        # bot.sendMessage(1190128536,str(e))


def market_order1(instrument):

    try:
        global quantity,data1

        ltp=ltp_price(instrument)
        for i in range(len(data1)):
            client=Client(data1[i][4],data1[i][5])
            data=client.futures_account_balance()
            percentage=data[i][3]
            for j in range(len(data)):
                
                if data[j]['asset']=='USDT':
                    p_l=float(data[j]['withdrawAvailable'])   
            quantity=(((float(percentage))/100) * p_l)/ltp
            quantity=quantity*1
            quantity=quantity*1000


            quantity=math.floor(quantity)

            quantity=quantity/1000
            quantity1[str(data1[i][0])]=quantity



            try:
                order = client.futures_create_order(
                    symbol=str(instrument),
                    side=Client.SIDE_SELL,
                    type=Client.ORDER_TYPE_MARKET,
                
                    
                    quantity=round(quantity,3))
            except Exception as e:
                # bot.sendMessage(1190128536,str(e))
                pass


    except Exception as e:
        print(str(e))






        


def close_position(instrument,order_type):
    global quantity1,data1
    try:
        for i in range(len(data1)):
            client=Client(data1[i][4],data1[i][5])



            if order_type=='squareoffsell':
               


                order = client.futures_create_order(
                symbol=str(instrument),
                side=Client.SIDE_SELL,
                type=Client.ORDER_TYPE_MARKET,


                quantity=round(float(quantity1[str(data1[i][0])]),3))

            if order_type=='squareoffbuy':
               


                order = client.futures_create_order(
                symbol=str(instrument),
                side=Client.SIDE_BUY,
                type=Client.ORDER_TYPE_MARKET,


                quantity=round(float(quantity1[str(data1[i][0])]),3))


    
    except Exception as e:
        print(str(e))
        # bot.sendMessage(1190128536,str(e))


# %%

def main():
    conn = sqlite3.connect('db.sqlite3')
    c= conn.cursor()

    c.execute("SELECT * FROM shop_bot1")

    data1=c.fetchall()
    conn.commit()

    conn.close()
    ltp=ltp_price(symbol)
    df=candle_initial(symbol,time_frame)
    signal=""
    if position=="":
        if df['SMA 10'][-1]>df['SMA 21'][-1] and df['SMA 10'][-1]<df['SMA 21'][-1]:
            price=ltp
            signal="sell"

        if df['SMA 10'][-1]<df['SMA 21'][-1] and df['SMA 10'][-1]>df['SMA 21'][-1]:
            price=ltp
            signal="buy"
 
    if position=="long":
        if ltp>price+price* float(take_profit/100):
            signal="squareoffsell"

        if ltp<price-price* float(stop_loss/100):
            signal="squareoffsell"


    if position=="short":
        if ltp<price-price* float(take_profit/100):
            signal="squareoffbuy"

        if ltp>price+price* float(stop_loss/100):
            signal="squareoffbuy"


    if signal=="buy":
        market_order(symbol)
    if signal=="sell":
        market_order1(symbol)

    if signal=="squanreoffsell":
        close_position(symbol,signal)

    if signal=="squanreoffbuy":
        close_position(symbol,signal)


signal=""
position=""
quantity1={}
while True:
    times1=time.time()
    try:

        main()

    except Exception as e:
        print(str(e))
     


