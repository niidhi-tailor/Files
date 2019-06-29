import mysql.connector
import time
import ast

start_time = time.perf_counter()
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="nid270998",
  database="wikipedia"
)
print('connected to database')
mycursor = mydb.cursor()

#function to display data from table
def display_data(query):
    mycursor.execute(query)
    cursor = mycursor.fetchall()
    for row in cursor:
        print(row)

#function to insert 6 article name,vital article,level,class,importance and topic into the database table
#Table name: articledesc
def insert_article_data(csvfile):
    line_no = 0                                                                                      #variable to count number of lines
    for line in open(csvfile, encoding='latin-1'):                                                   #opens csv file and loop to fetch each line in file
        line_no = line_no + 1
        if line_no==1:
            continue
        else:
            query = "insert into articledesc values("                                                  #string variable 'query' to store mysql query, creating insert query
            arr = line.split('@$@')                                                                    #spliting the file line fetched based on the deliminator '@$@'
            for i in range(0, 5):                                                                      #loop to fetch each value obtained after spliting the line
                if i == 0:
                    query = query + '"' + arr[i] + '"'
                else:
                    query = query + ',"' + arr[i] + '"'
            query = query + ");"
            print(line_no)
            mycursor.execute(query)                                                                     #executing query
        if line_no % 1000 == 0:
            mydb.commit()                                                                               #saving changes by every 1000 lines in database
    print("all data inserted")
    mydb.commit()                                                                                       #saving all changes in database



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
            temp = arr[5]                                                                                   #accessing the last value in the line , wikipedia projects, they are in the form an array

            if temp.startswith('NA'):                                                                       #if wikipedia project name not available
                    query = "insert into wiki_project(article_nm,project) values('" + title + "',NULL);"    #creating insert query
                    mycursor.execute(query)                                                                 #executing insert query
            else:                                                                                           #if wikipedia project name avaialble
                    arr2=ast.literal_eval(temp)                                                             #converting it into array
                    if arr2==[]:                                                                            #if array is empty
                        query = "insert into wiki_project(article_nm,project) values('"+ title + "',NULL);" #creating insert query
                        mycursor.execute(query)                                                             #executing insert query
                    else:                                                                                   #if array contains values
                        for val in arr2:
                            vali=val.replace("'","\\'")
                            query="insert into wiki_project(article_nm,project) values('"+title+"','"+vali+"');" #creating insert query
                            mycursor.execute(query)                                                         #executing insert query
            print(line_no)                                                                                  #print's the number of the line accessed in the file
        if line_no%1000 == 0:
            mydb.commit()                                                                                   #save changes to database after executing every 1000 lines
    print("all data inserted")
    mydb.commit()                                                                                           # saving the changes in the database




insert_article_data('articleDesc.csv')
print('Data inserted in articledesc')
insert_wiki_project('articleDesc.csv')
print("Data inserted in wiki_project")
print("Operation performed successfully")