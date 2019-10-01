import mysql.connector
import time

start_time = time.perf_counter()
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="nid270998",
  database="wikipedia"
)

print('connected to database')

mycursor = mydb.cursor(buffered=True)

#function to display data
def displaydata(query):
    mycursor.execute(query)
    cursor=mycursor.fetchall()
    for row in cursor:
        print(row)

#function to create table for change_tag file
def create_table():
    query="DROP TABLE IF EXISTS `redirect`;"
    query2="CREATE TABLE `redirect` ("\
  "`rd_from` int(8) unsigned NOT NULL DEFAULT '0',"\
  "`rd_namespace` int(11) NOT NULL DEFAULT '0',"\
  "`rd_title` varbinary(255) NOT NULL DEFAULT '',"\
  "`rd_interwiki` varbinary(32) DEFAULT NULL,"\
  "`rd_fragment` varbinary(255) DEFAULT NULL,"\
  "PRIMARY KEY (`rd_from`),"\
  "KEY `rd_ns_title` (`rd_namespace`,`rd_title`,`rd_from`)"\
") ENGINE=InnoDB DEFAULT CHARSET=binary;"
    mycursor.execute(query)
    mycursor.execute(query2)
    print("table created")
    mydb.commit();

#function to insert data from enwiki-latest-change_tag.sql file to the table in database
def insert_data(filename):
   line_no=0
   for line in open(filename,encoding='latin-1'):
        line_no=line_no+1
        if line.startswith('INSERT'):
            str = line.replace("'","\'")
            mycursor.execute(str)
            print(line_no)
   mydb.commit()
   print('all data inserted')


#create_table()
insert_data('C:\\Users\\NIDHI\\Desktop\\enwiki-20190901-redirect.sql')
#displaydata("select *from change_tag where ct_id=11000;")
print('Operation performed')
mydb.close()

