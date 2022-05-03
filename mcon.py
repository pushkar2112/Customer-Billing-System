import mysql.connector as mysql

#-------------------------ESTABLISHING CONNECTION--------------------------
mcon=mysql.connect(host='localhost', user='root', passwd='pushkar1', database='cbs')
if mcon.is_connected():
    print("Successfully connected")

curs=mcon.cursor()