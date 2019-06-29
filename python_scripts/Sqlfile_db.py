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

mycursor = mydb.cursor()

#function to display data
def displaydata(query):
    mycursor.execute(query)
    cursor=mycursor.fetchall()
    for row in cursor:
        print(row)

#function to create table for change_tag file
def create_table():
    query="DROP TABLE IF EXISTS `change_tag`;"
    query2="CREATE TABLE `change_tag` (" \
           "`ct_id` int(10) unsigned NOT NULL AUTO_INCREMENT," \
           "`ct_rc_id` int(11) DEFAULT NULL," \
           "`ct_log_id` int(10) unsigned DEFAULT NULL," \
           "`ct_rev_id` int(10) unsigned DEFAULT NULL," \
           "`ct_params` blob," \
           "`ct_tag_id` int(10) unsigned NOT NULL," \
           "PRIMARY KEY (`ct_id`)," \
           "UNIQUE KEY `change_tag_rc_tag_id` (`ct_rc_id`,`ct_tag_id`)," \
           "UNIQUE KEY `change_tag_log_tag_id` (`ct_log_id`,`ct_tag_id`)," \
           "UNIQUE KEY `change_tag_rev_tag_id` (`ct_rev_id`,`ct_tag_id`)," \
           "KEY `change_tag_tag_id_id` (`ct_tag_id`,`ct_rc_id`,`ct_rev_id`,`ct_log_id`)" \
           ") ENGINE=InnoDB AUTO_INCREMENT=75653274 DEFAULT CHARSET=binary;"
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
            str = line.replace("'","\\'")
            mycursor.execute(str)
            print(line_no)
   mydb.commit()
   print('all data inserted')


#create_table()
insert_data('enwiki-latest-category.sql')
#displaydata("select *from change_tag where ct_id=11000;")
print('Operation performed')
