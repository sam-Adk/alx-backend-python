#!/usr/bin/python3
import mysql.connector

def stream_users_in_batches(batch_size):
    """Generator that yields rows in batches from user_data table"""
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",  # change if needed
            database="ALX_prodev"
        )
    except mysql.connector.Error as err:
        print(f"Error connecting to database: {err}")
        return

    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM user_data;")

    batch = []
    for row in cursor:  # Loop 1: iterate over all rows
        batch.append(row)
        if len(batch) == batch_size:
            yield batch  # Yield a full batch
            batch = []

    if batch:  # Yield remaining rows if any
        yield batch

    cursor.close()
    connection.close()


def batch_processing(batch_size):
    """Process each batch and yield users over age 25"""
    for batch in stream_users_in_batches(batch_size):  # Loop 2: iterate over batches
        for user in batch:  # Loop 3: iterate over users in the batch
            if user['age'] > 25:
                print(user)
