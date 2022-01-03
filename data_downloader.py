#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import yfinance as yf
from datetime import date, timedelta


# In[2]:


def download_data():
    print("Valid time intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo")
    input2 = input("Enter time interval: ")
    input_ = input("Enter Ticker Symbol: ")
    df = yf.download(input_, 
                     start=(date.today().replace(day=1) - timedelta(30 * 61)), 
                     end=date.today().replace(day=1), 
                     progress=False,
                     interval=input2)
    df = df.rename(columns={df.columns[4]: input_})
    df = df[input_]
    stocks = []
    while input_ != "quit":
        input_ = input("Enter Ticker Symbol (enter \"quit\" to exit): ")
        if input_ != "quit":
            stocks.append(input_)
        
    for stock in stocks:
        df2 = yf.download(stock, 
                          start=(date.today().replace(day=1) - timedelta(30 * 61)), 
                          end=date.today().replace(day=1), 
                          progress=False,
                          interval=input2)
        df2 = df2.rename(columns = {df2.columns[4]: stock})
        df2 = df2[stock]
        df = pd.concat([df, df2], axis=1)
    for index,row in df.iterrows():
        delete = True
        for i in range(len(stocks) + 1):
            if not np.isnan(row[i]):
                delete = False
        if delete:
            df = df.drop(index)
    df.to_excel('output.xlsx')


# In[3]:


if __name__ == '__main__':
    download_data()







