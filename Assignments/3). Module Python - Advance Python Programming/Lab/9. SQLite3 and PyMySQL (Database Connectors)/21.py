# Practical Example 21: Write a Python program to create a database and a table using SQLite3.
import sqlite3

DB_NAME = "beginner_data.db"

# 1. Connect to the database (creates the file if it doesn't exist)
conn = sqlite3.connect(DB_NAME)
cursor = conn.cursor()

# 2. SQL command to create a table
create_table_sql = """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        role TEXT
    )
"""

# 3. Execute the command
cursor.execute(create_table_sql)

# 4. Save the changes
conn.commit()

# 5. Close the connection
conn.close()

print(f"Database '{DB_NAME}' created and table 'users' is ready.")
