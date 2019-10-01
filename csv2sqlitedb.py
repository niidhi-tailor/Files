# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 18:24:01 2019

@author: NIDHI
"""

import sqlite3

dbname=input("Enter datatbase name\n")                                         #database name
conn = sqlite3.connect(dbname)                                                 #creating connection with database
print('connected to database') 
    
#function to insert data in the table created
def insert_data(csvfile,tablename):
    delimiter=input("Enter deimiter\n")                                        #delimiter of csv file
    line_no = 0                                                                #counter to check number of lines of data inserted from the csv file
    for line in open(csvfile,encoding='latin-1'):                              #for loop to fetch each line from the file
        line_no = line_no + 1                                                  #incrementing line_no counter 
        str=line.replace('"',"'") 
        if line_no == 1:                                                       #first line of the file hence continue                                                                             
            continue
        else: 
            query = "insert into "+tablename+" values("                        #query string to form insert query                                                  
            arr = str.split(delimiter)                                         #array to store values after spliting the line using delimiter
            num_of_values=len(arr)                                             #number value after spliting the line with delimiter
            for i in range(0, num_of_values):                                  #for loop to add each value to query string                                                                      
                if i == 0:
                    query = query + '"' + arr[i] + '"'
                else:
                    query = query + ',"' + arr[i] + '"'
            query = query + ");"
            print(line_no)
            conn.execute(query)                                                #executing insert query
            conn.commit()                                                      #committing the changes after each value is inserted                                                                            #saving changes by every 1000 lines in database
    print("all data inserted")
    conn.commit()        

#function to create table
def create_table(csvfile):
    delimiter=input("Enter deimiter\n")                                        #delimiter of csv fiel
    tablename=input("Enter table name\n")                                      #table name in which data is to be inserted
    f=open(csvfile, encoding='latin 1')                                        #opening the csv file
    lines=f.readlines()                                                        #reading lines from file
    arr1=lines[0].split(delimiter)                                             #splitting first using delimiter
    arr2=lines[1].split(delimiter)                                             #spliting second line from file
    x=len(arr1)                                                                #x contains total number of values splitting 
    query="create table "+tablename+"("                                        #query string to form create table query 
    for i in range(0,x):                                                       #for loop to form create table query
        arr1[i]=arr1[i].replace(". ","_")
        arr1[i]=arr1[i].replace(" ","_")
        if i==x-1:
            if arr2[i].isdigit(): 
                 query=query+arr1[i]+" integer"
            else:
                query=query+arr1[i]+" text"            
        else:
             if arr2[i].isdigit():
                 query=query+arr1[i]+" integer,"
             else:
                query=query+arr1[i]+" text,"
    query=query+");"
    print(query)
    conn.execute(query)                                                        #executing create table querry
    conn.commit()                                                              #commiting changes
    print("table created\n") 
    
#function to display data from table
def display_data(query):
    cursor = conn.execute(query)
    for row in cursor:
        print(row)   
                                                                            
create_table('C://Users//NIDHI//Downloads//sample.csv')
insert_data('C://Users//NIDHI//Downloads//sample.csv',"sample")
print("Operation performed successfully")