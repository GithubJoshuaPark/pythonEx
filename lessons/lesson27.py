# lessons/lesson27.py
import sqlite3
import utils

utils.show_base_name(__file__, True)

def main():
    """
    This lesson demonstrates how to interact with an SQLite database using the sqlite3 module.
    This version uses an in-memory database to avoid file system issues.
    """
    conn = None  # Initialize conn to None

    print("--- Lesson 27: SQLite Database Access (In-Memory) ---")

    try:
        # 1. Connecting to an In-Memory Database
        # ':memory:' creates a temporary database in RAM. It's fast and automatically
        # cleaned up when the connection is closed.
        conn = sqlite3.connect(':memory:')
        print("Successfully connected to in-memory SQLite database.")

        # 2. Creating a Cursor and a Table
        cursor = conn.cursor()

        print("\n--- Creating a table 'users' ---")
        cursor.execute("""
            CREATE TABLE users (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                age INTEGER
            )
        """)
        print("Table 'users' created successfully.")

        # 3. Inserting Data (Create)
        print("\n--- Inserting data into 'users' ---")
        users_to_insert = [
            ('Alice', 'alice@example.com', 30),
            ('Bob', 'bob@example.com', 25),
            ('Charlie', 'charlie@example.com', 35)
        ]
        cursor.executemany("INSERT INTO users (name, email, age) VALUES (?, ?, ?)", users_to_insert)
        print(f"{cursor.rowcount} records inserted.")

        # 4. Querying Data (Read)
        print("\n--- Querying all users ---")
        cursor.execute("SELECT * FROM users")
        all_users = cursor.fetchall()
        for user in all_users:
            print(f"  - {user}")

        # 5. Updating Data (Update)
        print("\n--- Updating Bob's age to 26 ---")
        cursor.execute("UPDATE users SET age = ? WHERE name = ?", (26, 'Bob'))
        print(f"{cursor.rowcount} record(s) updated.")

        # Verify the update
        cursor.execute("SELECT * FROM users WHERE name = 'Bob'")
        updated_bob = cursor.fetchone()
        print(f"  - Updated Bob: {updated_bob}")

        # 6. Deleting Data (Delete)
        print("\n--- Deleting Charlie ---")
        cursor.execute("DELETE FROM users WHERE name = ?", ('Charlie',))
        print(f"{cursor.rowcount} record(s) deleted.")

        # Verify the deletion
        print("\n--- Querying all users after delete ---")
        cursor.execute("SELECT * FROM users")
        remaining_users = cursor.fetchall()
        for user in remaining_users:
            print(f"  - {user}")

    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        # Explicitly close the connection in the finally block
        if conn:
            conn.close()
            print("\nConnection explicitly closed.")

    print("-" * 20)
    utils.show_base_name(__file__, False)

if __name__ == "__main__":
    main()
else:
    utils.show_base_name(__file__, False)