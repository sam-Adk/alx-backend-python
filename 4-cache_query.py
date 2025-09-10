#!/usr/bin/env python3
"""
Task 4: Cache database queries with a decorator.
"""

import time
import sqlite3
import functools

# Global cache dictionary
query_cache = {}


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


def cache_query(func):
    """
    Decorator to cache query results based on the query string.
    Uses a global dictionary 'query_cache'.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        query = kwargs.get("query") if "query" in kwargs else None

        if query in query_cache:
            print(f"[CACHE HIT] Returning cached result for: {query}")
            return query_cache[query]

        print(f"[CACHE MISS] Executing and caching result for: {query}")
        result = func(*args, **kwargs)
        query_cache[query] = result
        return result

    return wrapper


@with_db_connection
@cache_query
def fetch_users_with_cache(conn, query):
    """Fetch users with caching enabled."""
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()


if __name__ == "__main__":
    # First call → executes query and caches
    users = fetch_users_with_cache(query="SELECT * FROM users")
    print(users)

    # Second call → uses cache, no DB query executed
    users_again = fetch_users_with_cache(query="SELECT * FROM users")
    print(users_again)
