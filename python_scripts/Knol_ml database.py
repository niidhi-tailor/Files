import sqlite3
import xml.etree.ElementTree as et

conn = sqlite3.connect('Wikipedia_db')
tree = et.parse('Post99.knolml')
root = tree.getroot()

#function to display data from table
def displaydata(query):
    cursor = conn.execute(query)                                #executing the query
    for row in cursor:                                          #displaying the data
        print(row)

#function to insert knowledge data details from a knolml file to the database
def insert_knowdata():
    type = root[0].get('Type')
    k_id = root[0].get('Id')
    title = root[0][0].text
    query = 'insert into know_data values("' + k_id + '","' + type + '","' + title + '");'
    conn.execute(query)
    conn.commit()
    print("Data inserted successfully")

#function to insert instance data in knolml file to the database
def insert_instancedata():
    k_id = root[0].get('Id')
    count1 = 0
    for child in root[0]:
        count1 = count1 + 1
    for i in range(1, count1):
        inst_id = root[0][i].get('Id')
        inst_type = root[0][i].get('InstanceType')
        c_date = ''
        ed_date = ''
        act_date = ''
        owner_id = ''
        editor_id = ''
        b_text = ''
        tags = ''
        score = '0'
        viewcount = '0'
        answercount = '0'
        commcount = '0'
        count2 = 0
        for child in root[0][i]:
            count2 = count2 + 1
        for j in range(count2):
            count3 = 0
            if root[0][i][j].tag == 'Tags':
                tags = root[0][i][j].text
            for child in root[0][i][j]:
                count3 = count3 + 1
                for k in range(count3):
                    if child.tag == 'CreationDate':
                        c_date = root[0][i][j][k].text
                    if child.tag == 'LastEditDate':
                        ed_date = root[0][i][j][k].text
                    if child.tag == 'LastActivityDate':
                        act_date = root[0][i][j][k].text
                    if child.tag == 'OwnerUserId':
                        owner_id = root[0][i][j][k].text
                    if child.tag == 'LastEditorUserId':
                        editor_id = root[0][i][j][k].text
                    if child.tag == 'Text':
                        str = root[0][i][j][k].text
                        b_text = str.replace("'", "''")
                    if child.tag == 'Score':
                        score = root[0][i][j][k].text
                    if child.tag == 'ViewCount':
                        viewcount = root[0][i][j][k].text
                    if child.tag == 'AnswerCount':
                        answercount = root[0][i][j][k].text
                    if child.tag == 'CommentCount':
                        commcount = root[0][i][j][k].text

        query = "insert into inst_data values(" + k_id + "," + inst_id + ",'" + inst_type + "','" + c_date + "','" + ed_date + "','" + \
                act_date + "','" + owner_id + "','" + editor_id + "','" + b_text + "','" + tags + "'," + score + "," + viewcount + "," + \
                answercount + "," + commcount + ");"
        # print(query)
        conn.execute(query)
        conn.commit()
        print("Instancec data inserted successfully")


'''
#Query to create table to store knowledge data
query1='CREATE TABLE KNOW_DATA' \
      '(K_ID INTEGER ,' \
       'TYPE TEXT,' \
       'TITLE TEXT,' \
       'PRIMARY KEY (K_ID));'
       
#Queries to create table to store instance data 
query2 = 'CREATE TABLE INST_DATA' \
         '(K_ID INTEGER NOT NULL ,' \
         'INST_ID INTEGER NOT NULL ,' \
         'INST_TYPE TEXT,' \
         'C_DATE DATE,' \
         'LAST_ED_DATE DATE,' \
         'LAST_ACT_DATE DATE,' \
         'OWNER_ID INTEGER,' \
         'EDITOR_ID INTEGER,' \
         'B_TEXT TEXT,' \
         'TAGS TEXT,' \
         'SCORE INTEGER,' \
         'VIEWCOUNT INTEGER,' \
         'ANSWERCOUNT INTEGER,' \
         'COMMCOUNT INTEGER,' \
         'PRIMARY KEY(K_ID,INST_ID),' \
         'FOREIGN KEY(K_ID) REFERENCES KNOW_DATA(K_ID));'
         
'''


insert_knowdata()
insert_instancedata()
displaydata()
print('Operation performed')
