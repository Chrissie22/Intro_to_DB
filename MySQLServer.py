import mysql.connector


try:
    db = mysql.connector.connect(
        user="root",
        host="localhost",
        password="Boo9475@"
    )

    cursor = db.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    db.commit()
    db.close()
    print("Database 'alx_book_store' created successfully!")
    
except mysql.connector.Error as e:
    print("{}: {}".format(e.__class__.__name__, e))