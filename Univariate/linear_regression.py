# -*- coding: utf-8 -*-
"""
Created on Fri Jan 30 11:50:50 2015

@author: kabadda
"""

import pandas as pd
loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')
import matplotlib.pyplot as plt
import scipy.stats as stats
import numpy as np
import statsmodels.api as sm

loansData['Interest.Rate']=map(lambda x: float(x[:-1])/100,loansData['Interest.Rate'])
loansData['Loan.Length']=map(lambda x: x.strip("months"),loansData['Loan.Length'])
loansData["FICO.Score"]=map(lambda x: float(x.replace("-",",").split(",")[0]),loansData['FICO.Range'])
#plt.figure()
#p=loansData["FICO.Score"].hist()
#plt.show()
##plt.figure()
#graph=stats.probplot(loansData['FICO.Score'],plot=plt)
#plt.show()

#pd.scatter_matrix(loansData, alpha=0.05, figsize=(10,10), diagonal='hist')
#plt.savefig(r"figure_1.png")

intrate = loansData['Interest.Rate']
loanamt = loansData['Amount.Requested']
fico = loansData['FICO.Score']
y = np.matrix(intrate).transpose()
x1 = np.matrix(fico).transpose()
x2 = np.matrix(loanamt).transpose()
x = np.column_stack([x1,x2])
X = sm.add_constant(x)
model = sm.OLS(y,X)
f = model.fit()
print 'Coefficients: ', f.params[0:2]
print 'Intercept: ', f.params[2]
print 'P-Values: ', f.pvalues
print 'R-Squared: ', f.rsquared