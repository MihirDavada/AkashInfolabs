import mysql.connector
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="mydb"
)
mycursor = conn.cursor()

# sql = "INSERT INTO tbl_user (user_firstname, user_lastname, user_address, user_email,user_password) VALUES ('Vivek', 'Sangadiya','MadhavPark, Shantivan Society', 'vicky@gmail.com', 123456);"
# mycursor.execute(sql)
# conn.commit()
# print(mycursor.rowcount, "row inserted.")


# mycursor.execute("SELECT * FROM tbl_student")
# myresult = mycursor.fetchall()
# for x in myresult:
#     print(x)


# sql = "UPDATE tbl_user SET user_firstname = 'Aarav' WHERE user_id  = 1"
# mycursor.execute(sql)
# conn.commit()
# print(mycursor.rowcount, "row updated")




# sql = "DELETE FROM tbl_user WHERE user_id = 2"
# mycursor.execute(sql)
# conn.commit()
# print(mycursor.rowcount, "row deleted")
