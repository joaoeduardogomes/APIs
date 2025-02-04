from execute_query import execute_query


#! GET
def get_data():
    query = """
        SELECT 
            books.id, 
            books.title, 
            books.genre, 
            books.isbn, 
            books.released_year, 
            GROUP_CONCAT(authors.id, ', ') as author_id, 
            GROUP_CONCAT(authors.name, ', ') as author_name, 
            GROUP_CONCAT(authors.country, ', ') as author_country
        FROM 
            books 
            JOIN books_authors ON books.id = books_authors.book_id 
            JOIN authors ON authors.id = books_authors.author_id
        GROUP BY
            books.id, books.title, books.genre, books.isbn, books.released_year
        ORDER BY   
            books.title;
    """
    rows = execute_query(query=query, fetch=True)

    if rows is not None:
        columns = [
            "book_id",
            "title",
            "genre",
            "isbn",
            "released_year",
            "author_id",
            "author_name",
            "author_country",
        ]
        return [dict(zip(columns, row)) for row in rows]
    return []


def get_data_by_book_id(book_id):
    query = """
        SELECT
            books.id,
            books.title,
            books.genre,
            books.isbn,
            books.released_year,
            GROUP_CONCAT(authors.id, ', ') AS author_id, 
            GROUP_CONCAT(authors.name, ', ') AS author_name, 
            GROUP_CONCAT(authors.country, ', ') AS author_country
        FROM
            books
            JOIN books_authors ON books.id = books_authors.book_id
            JOIN authors ON authors.id = books_authors.author_id
        WHERE
            books.id = ?
        GROUP BY
            books.id, books.title, books.genre, books.isbn, books.released_year
        ORDER BY
            books.title;
        """

    rows = execute_query(query=query, params=(book_id,), fetch=True)

    if rows is not None:
        columns = [
            "book_id",
            "title",
            "genre",
            "isbn",
            "released_year",
            "author_id",
            "author_name",
            "author_country",
        ]
        return [dict(zip(columns, row)) for row in rows]
    return []


def get_data_by_author_id(author_id):
    query = """
        SELECT
            books.id,
            books.title,
            books.genre,
            books.isbn,
            books.released_year,
            GROUP_CONCAT(authors.id, ', ') AS author_id, 
            GROUP_CONCAT(authors.name, ', ') AS author_name, 
            GROUP_CONCAT(authors.country, ', ') AS author_country
        FROM
            books
            JOIN books_authors ON books.id = books_authors.book_id
            JOIN authors ON authors.id = books_authors.author_id
        WHERE
            authors.id = ?
        GROUP BY
            books.id, books.title, books.genre, books.isbn, books.released_year
        ORDER BY
            books.title;
        """

    rows = execute_query(query=query, params=(author_id,), fetch=True)

    if rows is not None:
        columns = [
            "book_id",
            "title",
            "genre",
            "isbn",
            "released_year",
            "author_id",
            "author_name",
            "author_country",
        ]
        return [dict(zip(columns, row)) for row in rows]
    return []


#! POST
def add_data(book_id, author_id):
    query = "INSERT INTO books_authors (book_id, author_id) VALUES (?, ?)"
    execute_query(query, params=(book_id, author_id))


#! DELETE
def delete_data(book_id, author_id):
    query = "DELETE FROM books_authors WHERE book_id = ? AND author_id = ?"
    execute_query(query, (book_id, author_id))
