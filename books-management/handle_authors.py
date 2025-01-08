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
    query = """
        SELECT 
            id, 
            name, 
            country
        FROM 
            authors
        ORDER BY 
            SUBSTR(name, LENGTH(name) - INSTR(REPLACE(name, ' ', '_') || ' ', ' ') + 2);
    """
    rows = execute_query(query, fetch=True)
    
    if rows is not None:
        columns = ["id", "name", "country"]
        return [dict(zip(columns, row)) for row in rows]
    return []

#! GET
def get_author_by_id(author_id) -> dict:
    query = "SELECT id, name, country FROM authors WHERE id = ?"
    row = execute_query(query, params=(author_id,), fetch=True)
    
    if row:
        columns = ["id", "name", "country"]
        return dict(zip(columns, row[0]))
    return {}

#! GET
def get_author_by_name(name) -> dict:
    query = "SELECT id, name, country FROM authors WHERE LOWER(name) = ?"
    row = execute_query(query, params=(name.lower(),), fetch=True)
    
    if row:
        columns = ["id", "name", "country"]
        return dict(zip(columns, row[0]))
    return {}

#! GET
def get_country_authors(country) -> list:
    query = "SELECT id, name, country FROM authors WHERE LOWER(country) = ?"
    rows = execute_query(query, params=(country.lower(),), fetch=True)
    
    if rows is not None:
        columns = ["id", "name", "country"]
        return [dict(zip(columns, row)) for row in rows]
    return []

#! POST
def register_author(name, country):
    query = "INSERT INTO authors (name, country) VALUES (?, ?)"
    execute_query(query, params=(name, country))

#! PUT
def update_author(author_id, name, country) -> dict:
    query = "UPDATE authors SET name = ?, country = ? WHERE id = ?"
    execute_query(query=query, params=(name, country, author_id))
    return get_author_by_id(author_id)

#! DELETE
def delete_author(author_id) -> dict:
    query = "DELETE FROM authors WHERE id = ?"
    execute_query(query=query, params=(author_id,))