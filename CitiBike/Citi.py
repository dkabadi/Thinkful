# -*- coding: utf-8 -*-
"""
Created on Sat Feb 28 13:02:42 2015

@author: darshankabadi
"""

import sqlite3 as lite
import requests
from pandas.io.json import json_normalize
import time
from dateutil.parser import parse 
import collections


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





