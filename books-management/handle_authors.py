import sqlite3

def execute_query(query, params=(), fetch=False) -> list:

    try:
        with sqlite3.connect("management.db") as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            
            if fetch:
                return cursor.fetchall()
            else:
                conn.commit()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return None if not fetch else []


def get_authors():
    query = "SELECT id, firstname || ' ' || lastname AS name FROM authors"
    rows = execute_query(query, fetch=True)
    
    if rows is not None:
        columns = ["id", "firstname", "lastname"]
        return [dict(zip(columns, row)) for row in rows]
    return []



def register_author(firstname, lastname):
    query = "INSERT INTO authors (firstname, lastname) VALUES (?, ?)"
    execute_query(query, params=(firstname, lastname))
