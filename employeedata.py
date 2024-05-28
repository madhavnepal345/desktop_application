import sqlite3

def create_db():
    conn = sqlite3.connect('employees.db')
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            department TEXT NOT NULL,
            position TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

create_db()
