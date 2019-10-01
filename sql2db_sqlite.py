# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 19:25:36 2019

@author: NIDHI
"""

import sqlite3

conn = sqlite3.connect('Redirectdb.db')
print('connected to database')

#function to display data
def displaydata(query):
    cursor = conn.execute(query)  # executing the query
    for row in cursor:  # displaying the data
        print(row)

#function to create table for change_tag file
def create_table():
    query="DROP TABLE IF EXISTS `redirect`;"
    query2="CREATE TABLE `redirect` ("\
  "`rd_from` integer NOT NULL DEFAULT '0',"\
  "`rd_namespace` int(11) NOT NULL DEFAULT '0',"\
  "`rd_title` text NOT NULL DEFAULT '',"\
  "`rd_interwiki` text DEFAULT NULL,"\
  "`rd_fragment` text DEFAULT NULL,"\
  "PRIMARY KEY (`rd_from`));"
    conn.execute(query)
    conn.execute(query2)
    print("table created")
    conn.commit();

#function to insert data from enwiki-latest-change_tag.sql file to the table in database
def insert_data(filename):
   line_no=0
   for line in open(filename,encoding='latin-1'):
        line_no=line_no+1
        if line.startswith('INSERT'):
            str = line.replace("\\'","\\''")
            conn.execute(str)
            print(line_no)
            conn.commit()
   print('all data inserted')

create_table()

insert_data('C:\\Users\\NIDHI\\Documents\\newlines.txt')

conn.execute('DELETE FROM redirect;')
#conn.execute('select *from redirect limit 10')
#displaydata("select *from change_tag where ct_id=11000;")
print('Operation performed')
conn.close()

print('\')