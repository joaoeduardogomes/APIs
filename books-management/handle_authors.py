from execute_query import execute_query

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

#! GET
def list_authors_names() -> list:
    query = """
        SELECT name 
        FROM authors 
    """
    rows = execute_query(query, fetch=True)
    
    if rows is not None:
        return [row[0] for row in rows]
    return []

#! GET
def list_authors_countries() -> list:
    query = "SELECT DISTINCT country FROM authors ORDER BY country ASC"
    rows = execute_query(query, fetch=True)
    
    if rows is not None:
        return [row[0] for row in rows]
    return []

#! POST
def register_author(name, country):
    if not name or not country:
        raise ValueError("Both name and country are required.")

    query = "INSERT INTO authors (name, country) VALUES (?, ?)"
    execute_query(query, params=(name, country))

#! PUT
def update_author(author_id, name=None, country=None) -> dict:
    set_clauses = []
    params = []

    if name:
        set_clauses.append("name = ?")
        params.append(name)
    
    if country:
        set_clauses.append("country = ?")
        params.append(country)

    if not set_clauses:
        return {"error": "No fields provided to update"}

    query = f"UPDATE authors SET {', '.join(set_clauses)} WHERE id = ?"
    params.append(author_id)

    execute_query(query, params)

    return get_author_by_id(author_id)


#! DELETE
def delete_author(author_id) -> dict:
    query = "DELETE FROM authors WHERE id = ?"
    execute_query(query=query, params=(author_id,))