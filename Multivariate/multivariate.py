import pandas as pd
import numpy as np 
import statsmodels.formula.api as smf
import statsmodels.api as sm

df = pd.read_csv('LoanStats3c.csv', header=1, low_memory=False)
df=df.dropna()
df.int_rate=df['int_rate'].map(lambda x: float(str(x).strip("%"))/100)
x=df.annual_inc
y=df.int_rate

est1=smf.ols(formula='int_rate ~ annual_inc', data=df).fit()
est2=smf.ols(formula='int_rate ~ annual_inc + C(home_ownership)', data=df).fit()
est3=smf.ols(formula='int_rate ~ annual_inc * C(home_ownership)', data=df).fit()

