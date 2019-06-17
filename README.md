# FilesProject name: Knol-ML db
Knol_ml database.py can be used to insert and fetch data from the database named
Wikipedia_db.

The database has two tables
1) know_data
	columns: k_id,type,title
	-it stores knowledgedata id,type and title
2) inst_data
	columns: k_id,inst_id,inst_type,c_date,last_ed_date,last_act_date,owner_id,
		editor_id,b_text,tags,score,viewecount,nswercount,commcount
	-It stores all info related to an instance.

It consists of 3 functions:
1)insert_knowdata() - to insert data in know_data table
2)insert_instancedata() - to insert instance data in the table\
	To perform any of the above operations , add the file in knolml format 
	in the project . Change the file name in code line 5(tree=et.parse('filename.knolml'))
	and execute the function.
3)displaydata()- Display data is used to display data from the database.
	you can simply change the query in code line 10
	(cursor = conn.execute("select *from know_data;"))
	to fetch the desired data.

	The fetching queries that I performed were:
	1) select *from know_data; 
		- displays all data present in know_data table.

	2) select *from inst_data;
		-display all data present in inst_data table.

	3) select owner_id , editor_id from inst_data where k_id=1 and inst_id=1;
		-displays owner_is and editor_id from for instance id=1 and knowlege data id=1
		(you can change the column names after select to get the desired columns or 
		also could replace it '*from' to get all the data table  for the given 
		constraints after where clause)

	4) select title from know_data where k_id=99; 
		-displays title for knowledge id 99.

	5) select title from know_data JOIN inst_data on know_data.k_id = inst_data.k_id where owner_id='73'
		-this query will display title of the knowledgedata whose instnaces have owner_id as 73

all other select sql queries could be performed to get the desired output.
