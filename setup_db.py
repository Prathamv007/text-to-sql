import sqlite3

# Connect to SQLite (Creates a new file if it doesn't exist)
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# Create Users table
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    address TEXT NOT NULL
);
''')

# Insert sample data
cursor.executemany('''
INSERT INTO users (name, email, address) VALUES (?, ?, ?)
''', [
    ("Alice Johnson", "alice@example.com", "New York"),
    ("Bob Smith", "bob@example.com", "Los Angeles"),
    ("Charlie Brown", "charlie@example.com", "New York"),
    ("David Wilson", "david@example.com", "Chicago")
])

# Commit and close connection
conn.commit()
conn.close()

print("Database setup completed.")
