# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 21:12:17 2015

@author: darshankabadi
"""

import pandas as pd
import statsmodels.formula.api as smf
import statsmodels.api as sm
import numpy as np

from bs4 import BeautifulSoup
import requests
url = "http://web.archive.org/web/20110514112442/http://unstats.un.org/unsd/demographic/products/socind/education.htm"

r = requests.get(url)
soup = BeautifulSoup(r.content)
soup=soup('table')[6]
k=0
df=pd.DataFrame(columns=['Country','Year','Total','Men','Women'])
for i in soup.findAll('tr')[8:-11]:
     col=i.findAll('td')
     df.loc[k]= [col[0].text,col[1].text,col[4].text,col[7].text,col[10].text]
     k+=1
df.set_index('Country',inplace=True)

df2=pd.read_csv('ny.gdp.mktp.cd_Indicator_en_csv_v2.csv',skiprows=2,sep=',')
df2=pd.concat([df2['Country Name'],df2.ix[:,'1999':'2010']],1)

df2.set_index('Country Name',inplace=True)
final=df.join(df2)
final[['Total','Women','Men']]=final[['Total','Women','Men']].astype(int)
final.rename(columns={'2010':"regression"},inplace=True)

est1=smf.ols(formula='regression ~ Total', data=final).fit()
final=final[['Total','regression']]

final=final.dropna()
total=final.Total.values
reg=final.regression.values
scatter=plt.scatter(total,np.log10(reg),alpha=0.5)
(slope, intercept)=np.polyfit(total,np.log10(reg), 1)
plt.plot(total, total*slope + intercept, 'r')
