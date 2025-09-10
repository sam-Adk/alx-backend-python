#!/usr/bin/env python3
"""
Task 3: Retry database queries with a decorator.
"""

import time
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


def retry_on_failure(retries=3, delay=2):
    """
    Decorator factory to retry a function if it fails.
    :param retries: number of retry attempts
    :param delay: seconds to wait between retries
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempt = 0
            while attempt < retries:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempt += 1
                    print(f"[Retry {attempt}/{retries}] Error: {e}")
                    if attempt < retries:
                        time.sleep(delay)
                    else:
                        print("❌ All retries failed.")
                        raise
        return wrapper
    return decorator


@with_db_connection
@retry_on_failure(retries=3, delay=1)
def fetch_users_with_retry(conn):
    """Fetch all users with retry mechanism."""
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()


if __name__ == "__main__":
    try:
        users = fetch_users_with_retry()
        print("✅ Users fetched successfully:")
        for user in users:
            print(user)
    except Exception as e:
        print(f"❌ Could not fetch users: {e}")
