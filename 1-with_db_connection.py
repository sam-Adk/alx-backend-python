#!/usr/bin/env python3
"""
Task 1: Handle database connections with a decorator.
"""

import sqlite3
import functools


def with_db_connection(func):
    """Decorator to handle opening and closing database connections."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect("users.db")  # open connection
        try:
            # Pass the connection object as the first argument
            result = func(conn, *args, **kwargs)
        finally:
            conn.close()  # always close, even if error occurs
        return result
    return wrapper


@with_db_connection
def get_user_by_id(conn, user_id):
    """Fetch a user by ID from the database."""
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    return cursor.fetchone()


if __name__ == "__main__":
    # Example usage
    user = get_user_by_id(user_id=1)
    print(user)
