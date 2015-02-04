# -*- coding: utf-8 -*-
"""
Created on Sun Feb  1 16:54:19 2015

@author: darshankabadi
"""

from scipy import stats
import collections
import matplotlib.pyplot as plt

loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')
loansData.dropna(inplace=True)
freq = collections.Counter(loansData['Open.CREDIT.Lines'])
plt.figure()
plt.bar(freq.keys(), freq.values(), width=1)
plt.show()
chi, p = stats.chisquare(freq.values())