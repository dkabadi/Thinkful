# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 21:10:18 2015

@author: darshankabadi
"""

cities = { "Atlanta": '33.762909,-84.422675',
            "Austin": '30.303936,-97.754355',
            "Boston": '42.331960,-71.020173',
            "Chicago": '41.837551,-87.681844',
            "Cleveland": '41.478462,-81.679435'
        }
key="ea95f065e3a624efc009c013963fceab"

start_date=(datetime.datetime.today()-timedelta(days=30))
freq=pd.date_range(datetime.datetime.now()-timedelta(days=30),datetime.datetime.now())
cities2=cities.keys()
df=pd.DataFrame(index=freq,columns=cities2)
for i in range(31):
    Atlanta=requests.get("https://api.forecast.io/forecast/"+key+"/"+cities['Atlanta']+","+(start_date+timedelta(days=i)).strftime("%Y-%m-%dT%H:%M:%S"))    
    Austin=requests.get("https://api.forecast.io/forecast/"+key+"/"+cities['Austin']+","+(start_date+timedelta(days=i)).strftime("%Y-%m-%dT%H:%M:%S"))    
    Boston=requests.get("https://api.forecast.io/forecast/"+key+"/"+cities['Boston']+","+(start_date+timedelta(days=i)).strftime("%Y-%m-%dT%H:%M:%S"))    
    Chicago=requests.get("https://api.forecast.io/forecast/"+key+"/"+cities['Chicago']+","+(start_date+timedelta(days=i)).strftime("%Y-%m-%dT%H:%M:%S"))    
    Cleveland=requests.get("https://api.forecast.io/forecast/"+ key+"/"+cities['Cleveland']+","+(start_date+timedelta(days=i)).strftime("%Y-%m-%dT%H:%M:%S"))    
    Atlanta_Max=Atlanta.json()['daily'].values()[0][0]['apparentTemperatureMax']
    Austin_Max=Austin.json()['daily'].values()[0][0]['apparentTemperatureMax']
    Boston_Max=Boston.json()['daily'].values()[0][0]['apparentTemperatureMax']
    Chicago_Max=Chicago.json()['daily'].values()[0][0]['apparentTemperatureMax']
    Cleveland_Max=Cleveland.json()['daily'].values()[0][0]['apparentTemperatureMax']
    df['Boston'].ix[i]=Boston_Max
    df['Atlanta'].ix[i]=Atlanta_Max
    df['Cleveland'].ix[i]=Cleveland_Max
    df['Austin'].ix[i]=Austin_Max
    df['Chicago'].ix[i]=Chicago_Max
    
total_dif=abs(df.diff()).sum()
variance=df.var()