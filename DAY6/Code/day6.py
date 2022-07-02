import mysql.connector
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="mydb"
)
mycursor = conn.cursor()
# sql = "INSERT INTO tbl_student (st_name, st_email, st_mobile) VALUES ('Mihir', 'mihirdavada@gmail.com', 1234567890);"
# mycursor.execute(sql)
# conn.commit()
# print(mycursor.rowcount, "row inserted.")


# mycursor.execute("SELECT * FROM tbl_student")
# myresult = mycursor.fetchall()
# for x in myresult:
#     print(x)


# sql = "UPDATE tbl_student SET st_name = 'Aarav' WHERE st_id = 2"
# mycursor.execute(sql)
# conn.commit()
# print(mycursor.rowcount, "row updated")




# sql = "DELETE FROM tbl_student WHERE st_id = 2"
# mycursor.execute(sql)
# conn.commit()
# print(mycursor.rowcount, "row deleted")
