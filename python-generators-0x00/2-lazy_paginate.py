#!/usr/bin/python3
import seed

def paginate_users(page_size, offset):
    """Fetch a single page of users from the database"""
    connection = seed.connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    cursor.execute(f"SELECT * FROM user_data LIMIT {page_size} OFFSET {offset}")
    rows = cursor.fetchall()
    cursor.close()
    connection.close()
    return rows


def lazy_pagination(page_size):
    """Generator to lazily fetch pages of users"""
    offset = 0

    while True:  # Single loop
        page = paginate_users(page_size, offset)
        if not page:  # Stop if no more rows
            break
        yield page
        offset += page_size
