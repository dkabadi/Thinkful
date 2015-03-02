# -*- coding: utf-8 -*-
"""
Created on Sat Feb 21 12:09:23 2015

@author: darshankabadi
"""
import pandas as pd
import numpy as np 
import statsmodels.api as sm
import matplotlib.pyplot as plt
df = pd.read_csv('LoanStats3c.csv', header=1, low_memory=False)

# converts string to datetime object in pandas:
df['issue_d'] = pd.to_datetime(df['issue_d'])  
loan_count_summary = df.groupby('issue_d')['member_id'].count()
lags=loan_count_summary.size-1
statsmodels.api.graphics.tsa.plot_acf(loan_count_summary)

statsmodels.api.graphics.tsa.plot_pacf(loan_count_summary)

#arma_mod = sm.tsa.ARMA(lcs, (0,0)).fit()
#
#print(arma_mod.params)
#print(arma_mod.aic, arma_mod.bic, arma_mod.hqic)
#resids = arma_mod.resid.values
#
#fig = plt.figure(figsize=(12,8))
#ax = fig.add_subplot(111)
#ax = arma_mod.resid.plot(ax=ax);
#plt.savefig('resid_plot.png')
#
#dates = lcs.index
## start at a date on the index
#start = dates.get_loc(pandas.datetools.parse("1-1-20135"))
#end = start + 30 # "steps"
#pred = arma_mod.predict('2014-06-01', '2015-12-01') #need to supply frequency?!!
#
#fig, ax = plt.subplots(figsize=(12, 8))
#ax = lcs.ix['2009':].plot(ax=ax)
#fig = arma_mod.predict('2014-06-01', '2020-12-01').plot()#dynamic=True, ax=ax, plot_insample=False)