#!/usr/bin/python3
import seed

def stream_user_ages():
    """Generator that yields ages of users one by one"""
    connection = seed.connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT age FROM user_data;")
    
    for row in cursor:  # Loop 1: iterate over all rows
        yield row['age']
    
    cursor.close()
    connection.close()


def average_age():
    """Compute the average age using the generator"""
    total = 0
    count = 0
    
    for age in stream_user_ages():  # Loop 2: iterate over ages
        total += age
        count += 1

    if count == 0:
        print("No users found.")
        return

    avg = total / count
    print(f"Average age of users: {avg:.2f}")


if __name__ == "__main__":
    average_age()
