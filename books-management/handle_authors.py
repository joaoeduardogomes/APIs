import sqlite3

def get_authors():
    try:
        with sqlite3.connect("management.db") as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM authors")

            columns = [description[0] for description in cursor.description]
            rows = cursor.fetchall()

            return [dict(zip(columns, row)) for row in rows]
    except sqlite3.Error as e:
        print(f"Error fetching authors: {e}")
        return []

def register_author(firstname, lastname):
    try:
        with sqlite3.connect("management.db") as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO authors (firstname, lastname) VALUES (?, ?)", (firstname, lastname))
            conn.commit()
    except sqlite3.Error as e:
        print(f"Error inserting author: {e}")