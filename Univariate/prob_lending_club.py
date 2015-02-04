# -*- coding: utf-8 -*-
"""
Created on Tue Jan 27 13:42:45 2015

@author: darshankabadi
"""

import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats

loansData=pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')
loansData.dropna(inplace=True)
loansData.boxplot(column="Amount.Requested" )
plt.show()
loansData.hist(column="Amount.Requested" )
plt.show()
plt.figure()
graph=stats.probplot(loansData["Amount.Requested"],plot=plt)
plt.show()