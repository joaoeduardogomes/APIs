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

#! GET
def get_authors():
    query = "SELECT id, firstname || ' ' || lastname AS name FROM authors"
    rows = execute_query(query, fetch=True)
    
    if rows is not None:
        columns = ["id", "name"]
        return [dict(zip(columns, row)) for row in rows]
    return []

#! GET
def get_author_by_id(author_id) -> dict:
    query = "SELECT id, firstname || ' ' || lastname AS name FROM authors WHERE id = ?"
    row = execute_query(query, params=(author_id,), fetch=True)
    
    if row:
        columns = ["id", "name"]
        return dict(zip(columns, row[0]))
    return {}

#! POST
def register_author(firstname, lastname):
    query = "INSERT INTO authors (firstname, lastname) VALUES (?, ?)"
    execute_query(query, params=(firstname, lastname))

#! PUT
def update_author(author_id, firstname, lastname) -> dict:
    query = "UPDATE authors SET firstname = ?, lastname = ? WHERE id = ?"
    execute_query(query=query, params=(firstname, lastname, author_id))
    return get_author_by_id(author_id)