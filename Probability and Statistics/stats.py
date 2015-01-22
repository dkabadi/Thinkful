import pandas as pd
from scipy import stats
data = '''Region, Alcohol, Tobacco
North, 6.47, 4.03
Yorkshire, 6.13, 3.76
Northeast, 6.19, 3.77
East Midlands, 4.89, 3.34
West Midlands, 5.63, 3.47
East Anglia, 4.52, 2.92
Southeast, 5.89, 3.20
Southwest, 4.79, 2.71
Wales, 5.27, 3.53
Scotland, 6.08, 4.51
Northern Ireland, 4.02, 4.56'''

data=data.splitlines()
data=[i.split(", ") for i in data]
cols=data[0]
del data[0]
df=pd.DataFrame(data, columns=cols)
df['Alcohol']=df['Alcohol'].astype(float)
df['Tobacco']=df['Tobacco'].astype(float)
alc_mean=df['Alcohol'].mean()
alc_std=df['Alcohol'].std()
alc_var=df['Alcohol'].var()
alc_median=df['Alcohol'].median()
alc_mode=stats.mode(df['Tobacco'])
alc_range=max(df['Alcohol'])-min(df['Alcohol'])
tob_mean=df['Tobacco'].mean()
tob_std=df['Tobacco'].std()
tob_var=df['Tobacco'].var()
tob_median=df['Tobacco'].median()
tob_mode=stats.mode(df['Tobacco'])
tob_range=max(df['Tobacco'])-min(df['Tobacco'])
print "The mean for Alcohol and Tobacco respectively is", alc_mean, "and", tob_mean
print "The standard deviation for Alcohol and Tobacco respectively is", alc_std, "and", tob_std
print "The variance for Alcohol and Tobacco respectively is", alc_var, "and", tob_var
print "The median for Alcohol and Tobacco respectively is", alc_median, "and", tob_median
print "The mode for Alcohol and Tobacco respectively is", alc_mode, "and", tob_mode
print "The range for Alcohol and Tobacco respectively is", alc_range, "and", tob_range
