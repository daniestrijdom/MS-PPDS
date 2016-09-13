#!/usr/bin/env python

import sqlite3

conn = sqlite3.connect("test.db")
c = conn.cursor()

c.execute("DROP TABLE rates")

day = 0
c.execute('''
CREATE TABLE rates (
id FLOAT,
usd FLOAT,
repo FLOAT,
eur FLOAT
)
'''
)

with open("data.txt") as data:
    for line in data.readlines()[1:]:
        values = line.strip('\n').split(',')

        if (values[0]):
            #values[0] = values[0].replace("/","-")
            c.execute(
            '''
            INSERT INTO rates (id, usd, repo, eur)
            VALUES (%d, %f, %f, %f)
            '''
            % (day, float(values[1]), float(values[2]), float(values[3])
            )
            )
        day+=1
conn.commit()
conn.close()
