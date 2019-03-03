
import csv, sqlite3

connection = sqlite3.connect("studentt.db")

# cursor
crsr = connection.cursor()

# SQL command to create a table in the database
sql_command = """CREATE TABLE `stud` (
  studid varchar(255) NOT NULL default '',
  studnm varchar(255) default NULL,
  address varchar(255) default NULL,
  state varchar(255) default NULL,
  city varchar(255) default NULL,
  contact_no varchar(255) default NULL,
  gender varchar(255) default NULL,
  birthdate datetime default NULL,
  sem_no smallint(6) default NULL,
  branch varchar(255) default NULL,
  PRIMARY KEY  (`studid`)
);"""

# execute the statement
crsr.execute(sql_command)

with open('stud.csv') as fin: # `with` statement available in 2.5+
    # csv.DictReader uses first line in file for column headings by default
    dr = csv.DictReader(fin) # comma is default delimiter
    to_db = [(i['studid'], i['studnm'], i['address'], i['state'], i['city'], i['contact_no'], i['gender'], i['birthdate'], i['sem_no'], i['branch']) for i in dr]

#cur.executemany("INSERT INTO t (col1, col2) VALUES (?, ?);", to_db)
sql_command = """insert into `stud` (`studid`,`studnm`,`address`,`state`,`city`,`contact_no`,`gender`,`birthdate`,`sem_no`,`branch`) VALUES (?, ?,?, ?,?, ?,?, ?,?, ?)"""
crsr.executemany(sql_command,to_db)
connection.commit()
connection.close()
