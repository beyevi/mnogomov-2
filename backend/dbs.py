"""
Python module to handle Mnogomov's DBS
"""


import mysql.connector


mnogomov_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root"
)
db_cursor = mnogomov_db.cursor()


if __name__ == "__main__":
    db_cursor.execute("CREATE DATABASE IF NOT EXISTS mnogomov_db")
    db_cursor.execute("SHOW DATABASES")

    for x in db_cursor:
        print(x)
