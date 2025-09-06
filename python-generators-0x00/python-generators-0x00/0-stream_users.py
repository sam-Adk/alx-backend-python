#!/usr/bin/python3
import mysql.connector

def stream_users():
    """Generator that yields rows from the user_data table one by one"""
    
    # Connect to the ALX_prodev database
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Adikah1234@",  # change if needed
            database="ALX_prodev"
        )
    except mysql.connector.Error as err:
        print(f"Error connecting to database: {err}")
        return

    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM user_data;")

    # Single loop: yield each row one by one
    for row in cursor:
        yield row

    cursor.close()
    connection.close()
