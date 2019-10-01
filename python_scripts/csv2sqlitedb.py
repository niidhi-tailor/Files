# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 17:39:37 2019

@author: NIDHI
"""

import sqlite3
import time
import ast

start_time = time.perf_counter()
conn = sqlite3.connect('articleDescdb.db')
print('connected to database')

#create table queries
#conn.execute("CREATE TABLE article_desc(article_id number,article_nm text,vital_article text,level text,class tex,topic text);")
#conn.execute("CREATE TABLE wiki_project(article_nm text,project text)")   

#function to display data from table
def display_data(query):
    cursor = conn.execute(query)
    for row in cursor:
        print(row)

#function to insert 6 article name,vital article,level,class,importance and topic into the database table
#Table name: articledesc
def insert_article_data(csvfile):
    line_no = 0                                                                                      #variable to count number of lines
    for line in open(csvfile, encoding='latin-1'):                                                   #opens csv file and loop to fetch each line in file
        line_no = line_no + 1
        str=line.replace('"',"'")
        if line_no == 1:                                                                             #as first row in the file contains column name we skip the first row for inserting
            continue
        else:
            query = "insert into article_desc values("                                                  #string variable 'query' to store mysql query, creating insert query
            arr = str.split('@$@')                                                                    #spliting the file line fetched based on the deliminator '@$@'. Storing each valuein an array
            for i in range(0, 6):                                                                      #loop to fetch first 6 values in each line obtained after spliting the line 
                if i == 0:
                    query = query + '"' + arr[i] + '"'
                else:
                    query = query + ',"' + arr[i] + '"'
            query = query + ");"
            print(line_no)
            conn.execute(query)                                                                     #executing query
        if line_no % 1000 == 0:
            conn.commit()                                                                               #saving changes by every 1000 lines in database
    print("all data inserted")
    conn.commit()                                                                                       #saving all changes in database



#function to insert article name and wiki projects into the database
#table name wiki_project
def insert_wiki_project(csvfile):
    line_no = 0                                                                                             #variable to count number of lines
    for line in open(csvfile, encoding='latin-1'):                                                          #opens csv file, and loop to fetch each line in file
        line_no = line_no + 1
        if line_no==1:
            continue
        else:
            arr=line.split('@$@')                                                                           #splites the value in the csv file based on the deliminator"@$@"
            title = arr[0].replace("'", "\\'")                                                              #escaping single inverted commas as a part of value
            temp = arr[6]                                                                                   #accessing the last value in the line , wikipedia projects, they are in the form an array

            if temp.startswith('NA'):                                                                       #if wikipedia project name not available
                    query = "insert into wiki_project(article_nm,project) values('" + title + "',NULL);"    #creating insert query
                    conn.execute(query)                                                                 #executing insert query
            else:                                                                                           #if wikipedia project name avaialble
                    arr2=ast.literal_eval(temp)                                                             #converting it into array
                    if arr2==[]:                                                                            #if array is empty
                        query = "insert into wiki_project(article_nm,project) values('"+ title + "',NULL);" #creating insert query
                        conn.execute(query)                                                             #executing insert query
                    else:                                                                                   #if array contains values
                        for val in arr2:
                            vali=val.replace("'","''")
                            print(vali)
                            query="insert into wiki_project(article_nm,project) values('"+title+"','"+vali+"');" #creating insert query
                            conn.execute(query)                                                         #executing insert query
            print(line_no)                                                                                  #print's the number of the line accessed in the file
        if line_no%1000 == 0:
            conn.commit()                                                                                   #save changes to database after executing every 1000 lines
    print("all data inserted")
    conn.commit()                                                                                           # saving the changes in the database




#insert_article_data('C:\\Users\\NIDHI\\Documents\\articleDesc.csv')
#insert_wiki_project('C:\\Users\\NIDHI\\Documents\\articleDesc.csv')
display_data("select *from article_desc limit 10;")
print('Data inserted in articledesc')
print("Operation performed successfully")