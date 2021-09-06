import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", password="", database="mydata")
mydata = mydb.cursor()
select = ("SELECT * from user")
mydata.execute(select)
dataresult = mydata.fetchall()
for mdata in dataresult:
    x = mdata[3]
    print(x)