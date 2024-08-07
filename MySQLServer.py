import mysql.connector
from mysql.connector import Error


try:
    db = mysql.connector.connect(
        user="root",
        host="localhost",
        password="Boo9475@"
    )

    cursor = db.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store;")
    db.commit()
    db.close()
    print("Database 'alx_book_store' created successfully")
except Error as e:
    print("{}: {}".format(e.__class__.__name__, e))