from datetime import datetime
from execute_query import execute_query

def get_books():
    query = "SELECT * FROM books"
    rows = execute_query(query=query, fetch=True)

    if rows is not None:
        columns = ["id", "title", "genre", "isbn", "released_year"]
        return [dict(zip(columns, row)) for row in rows]
    return []

def get_book_by_id(book_id):
    query = "SELECT * FROM books WHERE id = ?"
    row = execute_query(query=query, params=(book_id,), fetch=True)

    if row:
        columns = ["id", "title", "genre", "isbn", "released_year"]
        return dict(zip(columns, row[0]))
    return {}

def get_book_by_title(title):
    query = "SELECT * FROM books WHERE LOWER(title) LIKE ?"
    rows = execute_query(query=query, params=(f"%{title.lower()}%",), fetch=True)

    if rows:
        columns = ["id", "title", "genre", "isbn", "released_year"]
        return [dict(zip(columns, row)) for row in rows]
    return {}

def add_book(title, genre, isbn, released_year):
    current_year = datetime.now().year
    if not (1500 <= released_year <= current_year):
        raise ValueError("Invalid released year. It must be between 1500 and the current year.")

    query = "INSERT INTO books (title, genre, isbn, released_year) VALUES (?, ?, ?, ?)"
    execute_query(query, params=(title, genre, isbn, released_year))