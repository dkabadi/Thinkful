# -*- coding: utf-8 -*-
"""
Created on Sat Feb 28 13:02:42 2015

@author: darshankabadi
"""

import sqlite3 as lite
import requests
import pandas as pd
from pandas.io.json import json_normalize
import time
from dateutil.parser import parse 
import collections
from datetime import timedelta
import matplotlib.pyplot as plt



r = requests.get('http://www.citibikenyc.com/stations/json')
df = json_normalize(r.json()['stationBeanList'])
con=lite.connect("citi_bike.db")

with con:
    cur=con.cursor()
    cur.execute('drop table if exists citibike_reference')
    cur.execute('CREATE TABLE citibike_reference (id INT PRIMARY KEY, totalDocks INT, city TEXT, altitude INT, stAddress2 TEXT, longitude NUMERIC, postalCode TEXT, testStation TEXT, stAddress1 TEXT, stationName TEXT, landMark TEXT, latitude NUMERIC, location TEXT )')

insert_citi = "INSERT INTO citibike_reference VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)"

with con:
    for station in r.json()['stationBeanList']:
        cur.execute(insert_citi,[station['id'],station['totalDocks'],station['city'],station['altitude'],station['stAddress2'],station['longitude'],station['postalCode'],station['testStation'],station['stAddress1'],station['stationName'],station['landMark'],station['latitude'],station['location']])

station_ids = df['id'].tolist() 
station_ids = ['_' + str(i) + ' INT' for i in station_ids]
exec_time = parse(r.json()['executionTime'])
id_bikes = collections.defaultdict(int)
for station in r.json()['stationBeanList']:
    id_bikes[station['id']] = station['availableBikes']

with con:
    cur.execute('drop table if exists available_bikes')
    cur.execute("CREATE TABLE available_bikes ( execution_time INT, " +  ", ".join(station_ids) + ")")
    cur.execute('INSERT INTO available_bikes (execution_time) VALUES (?)', (exec_time.strftime('%s'),))
    for k, v in id_bikes.iteritems():
        cur.execute("UPDATE available_bikes SET _" + str(k) + " = " + str(v) + " WHERE execution_time = " + exec_time.strftime('%s') + ";")


cur.execute("DELETE FROM available_bikes")
for i in range(60):
    r = requests.get('http://www.citibikenyc.com/stations/json')
    exec_time = parse(r.json()['executionTime'])
    cur.execute('INSERT INTO available_bikes (execution_time) VALUES (?)', (exec_time.strftime('%s'),))
    con.commit()
    id_bikes_new = collections.defaultdict(int)
    for station in r.json()['stationBeanList']:
        id_bikes_new[station['id']] = station['availableBikes'] 
    for k,v in id_bikes_new.iteritems():
        cur.execute("UPDATE available_bikes SET _" + str(k) + " = " + str(v) + " WHERE execution_time = " + exec_time.strftime('%s') + ";")
    time.sleep(60)

df = pd.read_sql_query("SELECT * FROM available_bikes ORDER BY execution_time",con,index_col='execution_time')
max_station=abs(df.diff()).sum().idxmax()[1:]
cur.execute("SELECT id, stationname, latitude, longitude FROM citibike_reference WHERE id = ?", (max_station,)
data = cur.fetchone()