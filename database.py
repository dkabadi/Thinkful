import sqlite3 as lite
import pandas as pd

con=lite.connect("getting_started.db")

cities= (("New York City","NY"),("Boston", "MA"),("Chicago","IL"),("Miami","FL"),("Dallas","TX"), ("Seattle", "Washington"), ("Portland","Oregon"), ("San Francisco","CA"), ("Los Angeles","CA"))
weather = (("New York City",2013,"July","January",62),("Boston",2013,"July","January",59),("Chicago",2013,"July","January",59),("Miami",2013,"August","January",84),("Dallas",2013,"July","January",77),
("Seattle",2013,"July","January",61), ("Portland",2013,"July","December",63),("San Francisco",2013,"September","December",64), ("Los Angeles",2013,"September","December",75))


    
with con:
    answer= raw_input("What city do you want to know information about?")
    cur=con.cursor()
    cur.execute('drop table if exists weather')
    cur.execute('drop table if exists cities')
    cur.execute('create table weather (city text, year integer, warm_month text, cold_month text, average_high integer)')
    cur.execute('create table cities ( name text, state text)')
    cur.executemany('insert into weather values (?,?,?,?,?)',weather)
    cur.executemany('insert into cities values (?,?)',cities)
    cur.execute("select city, state, year, warm_month, cold_month, average_high from cities inner join weather on name=city") 
    result=cur.fetchall()
    cols=[i[0] for i in cur.description]
    df = pd.DataFrame(result, columns = cols)
    cur.execute("select * from weather where city='%s'" %answer)
    result2=cur.fetchall()
    print result2
    