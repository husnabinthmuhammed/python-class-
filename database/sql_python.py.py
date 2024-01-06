import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="root",password="Husna@12",port=3306)
print(mydb)
mycursur = mydb.cursor()
#mycursur.execute("Create database maypython")
mycursur.execute("use maypython")
mycursur.execute("create table students(name varchar(250),age int,roll_num int)")
#sql = "INSERT INTO students(name,age,roll_num) VALUES (%s,%s,%s)"
#val = ("john",13,21)
mycursur.execute(sql,val)
mydb.commit()

print(mycursur.rowcount,"record inserted.")