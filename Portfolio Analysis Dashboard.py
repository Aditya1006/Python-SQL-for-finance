#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 10:54:45 2024

@author: Aditya1006
"""

import streamlit as st
import pandas as pd
import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
st.title('Investment Analysis Dashboard')

assets = st.text_input('Provide your assets (comma-separated)',"AAPL,MSFT,GOOGL")
start=st.date_input('Please provide a starting date for your analysis',value=pd.to_datetime('2022-06-01'))
data=yf.download(assets,start=start)['Adj Close']
data