# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import krakenex
import numpy
import time




pair = 'XETHZUSD'

k = krakenex.API()
k.load_key('kraken.key')

def update():
    while True:
        tradeData = k.query_public('OHLC', {'pair': pair, 'interval' : '60'})
        
        tradeArray = tradeData['result'][pair]
        size = len(tradeArray)
        
        close = []
        
        
        for x in range(size-21, size-1):
            close.append(float(tradeArray[x][4]))
            
        
        SMA = numpy.mean(close)
        std = numpy.std(close)
        
        BollingerL = SMA-(2*std)
        BollingerM = SMA
        BollingerH = SMA+(2*std)
        
        t_end = time.time() + 60 * 60
        while time.time() < t_end:
            tradeData = k.query_public('Ticker', {'pair': pair})
            tradeArray = tradeData['result'][pair]
            close = float(tradeData['result'][pair]['c'][0])
            
            if close > BollingerH:
                print("above high")
            if close > BollingerM and close < BollingerH:
                print("above medium and below high")
            if close < BollingerM and close > BollingerL:
                print("below medium and above low")
            if close < BollingerL:
                print("below low")
                
            print(close)
            time.sleep(60)
        
        
        print(BollingerL,BollingerM,BollingerH)
        time.sleep(60)
     
        
update()
