# -*- coding: utf-8 -*-
"""
Created on Mon Jan 26 22:57:36 2015

@author: darshankabadi
"""

import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats


loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')
loansData.dropna()
loansData.boxplot(column="Amount.Funded.By.Investors")
plt.show()
loansData.hist(column='Amount.Funded.By.Investors')
plt.show()
plt.figure()
graph=stats.probplot(loansData['Amount.Funded.By.Investors'],dist="norm", plot=plt)
plt.show()