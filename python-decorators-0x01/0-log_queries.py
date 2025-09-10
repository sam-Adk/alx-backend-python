#!/usr/bin/env python3
"""
Task 0: Logging database queries with a decorator.
"""

import sqlite3
import functools


def log_queries(func):
    """Decorator to log SQL queries before executing them."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Try to extract the query argument if present
        query = kwargs.get("query") if "query" in kwargs else (args[0] if args else None)
        if query:
            print(f"[LOG] Executing SQL Query: {query}")
        else:
            print("[LOG] Executing function without explicit SQL query")
        return func(*args, **kwargs)
    return wrapper


@log_queries
def fetch_all_users(query):
    """Fetch all users from the database."""
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results


if __name__ == "__main__":
    # Example usage
    users = fetch_all_users(query="SELECT * FROM users")
    for user in users:
        print(user)

