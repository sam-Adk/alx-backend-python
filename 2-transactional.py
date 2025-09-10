#!/usr/bin/env python3
"""
Task 2: Transaction Management Decorator.
"""

import sqlite3
import functools


def with_db_connection(func):
    """Decorator to handle opening and closing database connections."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect("users.db")
        try:
            result = func(conn, *args, **kwargs)
        finally:
            conn.close()
        return result
    return wrapper


def transactional(func):
    """
    Decorator to manage database transactions.
    Commits if successful, rolls back if an exception occurs.
    """
    @functools.wraps(func)
    def wrapper(conn, *args, **kwargs):
        try:
            result = func(conn, *args, **kwargs)
            conn.commit()   # commit if no error
            return result
        except Exception as e:
            conn.rollback()  # rollback on failure
            raise e
    return wrapper


@with_db_connection
@transactional
def update_user_email(conn, user_id, new_email):
    """Update a user's email in the database."""
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET email = ? WHERE id = ?", (new_email, user_id))


if __name__ == "__main__":
    # Example usage
    try:
        update_user_email(user_id=1, new_email="Crawford_Cartwright@hotmail.com")
        print("✅ Email updated successfully.")
    except Exception as e:
        print(f"❌ Failed to update email: {e}")
