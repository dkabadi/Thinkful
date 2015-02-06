# -*- coding: utf-8 -*-
"""
Created on Thu Feb 05 12:00:28 2015

@author: kabadda
"""

import statsmodels.api as sm
import pandas as pd

df=pd.read_csv('loansData_clean.csv')
df["Interest Rate <12%"]=df['Interest.Rate']<.12
df["Intercept"]=1.0

ind_vars=["FICO.Score","Amount.Requested","Intercept"]

logit = sm.Logit(df["Interest Rate <12%"], df[ind_vars])
result = logit.fit()    
coeff = result.params 
print coeff

def logistic_function(coeff,FICO,Requested):
    p = 1/(1 + 2.71828**(coeff[2] + coeff[0]*FICO + coeff[1]*Requested))
    return p
    
y=logistic_function(coeff,720,10000)

def pred(y):
    if y>.7:
        print "You will get a low interest rate"
    else:
        print "You will not get a low interest rate"
        
pred(y)