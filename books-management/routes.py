from flask import Flask, request, jsonify
import sqlite3
import handle_authors
import handle_books
import handle_books_authors


def register_routes(app):

    #! AUTHORS ROUTES
    #? GET
    @app.route("/authors", methods=["GET"])
    def get_authors():
        authors = handle_authors.get_authors()
        return jsonify(authors)

    #? GET
    @app.route("/authors/name/<string:name>", methods=["GET"])
    def get_author_by_name(name):
        author = handle_authors.get_author_by_name(name)
        return jsonify(author)

    #? GET
    @app.route("/authors/name", methods=["GET"])
    def list_authors_names():
        names = handle_authors.list_authors_names()
        return {"names": (names)}

    #? GET
    @app.route("/authors/country/<string:country>", methods=["GET"])
    def get_country_authors(country):
        authors = handle_authors.get_country_authors(country)
        return jsonify(authors)

    #? GET
    @app.route("/authors/country", methods=["GET"])
    def list_authors_countries():
        countries = handle_authors.list_authors_countries()
        return {"countries": (countries)}
    
    #? GET
    @app.route("/authors/<int:author_id>", methods=["GET"])
    def get_author_by_id(author_id):
        author = handle_authors.get_author_by_id(author_id)
        if not author:
            return jsonify({"error": f"Error: author not found"}), 400

        return jsonify(author)

    #? POST
    @app.route("/authors", methods=["POST"])
    def add_author():
        data = request.get_json()
        name = data["name"]
        country = data["country"]

        try:
            handle_authors.register_author(name, country)
            return jsonify({"message": f"Author: {name} registered!"}), 201
        except Exception as e:
            return jsonify({"error": f"Error: {e}"}), 400


    #? PUT
    @app.route("/authors/<int:author_id>", methods=["PUT"])
    def update_author(author_id):
        data = request.get_json()

        if not data:
            return jsonify({"error": "No data provided in the request body"}), 400

        name = data.get("name")
        country = data.get("country")

        try:
            updated_author = handle_authors.update_author(author_id, name, country)
            if "error" in updated_author:
                return jsonify(updated_author), 400
            return jsonify(updated_author)
        except Exception as e:
            return jsonify({"error": f"Error: {str(e)}"}), 400

    #? DELETE
    @app.route("/authors/<int:author_id>", methods=["DELETE"])
    def delete_author(author_id):
        author = handle_authors.get_author_by_id(author_id)
        if not author:
            return jsonify({"error": f"Error: author not found"}), 400

        try:
            handle_authors.delete_author(author_id)
            return jsonify({"message": f"Author '{author['name']}' deleted!"})
        except Exception as e:
            return jsonify({"error": f"Error: {str(e)}"}), 500
        

    
    #! BOOKS ROUTES
    #? GET
    @app.route("/books", methods=["GET"])
    def get_books():
        books = handle_books.get_books()
        return jsonify(books)
    
    #? GET
    @app.route("/books/<int:book_id>", methods=["GET"])
    def get_book_by_id(book_id):
        book = handle_books.get_book_by_id(book_id)
        return jsonify(book)
    
    #? GET
    @app.route("/books/<string:title>", methods=["GET"])
    def get_book_by_title(title):
        book = handle_books.get_book_by_title(title)
        return jsonify(book)

    #? POST
    @app.route("/books", methods=["POST"])
    def add_book():
        data = request.get_json()
        title = data["title"]
        genre = data["genre"]
        isbn = data.get("isbn", None)
        released_year = data["released_year"]

        try:
            handle_books.add_book(title, genre, isbn, released_year)
            return jsonify({"message": f"Book: {title} registered!"}), 201
        except Exception as e:
            return jsonify({"error": f"Error: {e}"}), 400
        
    #? PUT
    @app.route("/books/<int:book_id>", methods=["PUT"])
    def update_book(book_id):
        data = request.get_json()

        if not data:
            return jsonify({"error": "No data provided in the request body"}), 400

        title = data.get("title")
        genre = data.get("genre")
        isbn = data.get("isbn")
        released_year = data.get("released_year")

        try:
            updated_book = handle_books.update_book(book_id, title, genre, isbn, released_year)
            if "error" in updated_book:
                return jsonify(updated_book), 400
            return jsonify(updated_book)
        except Exception as e:
            return jsonify({"error": f"Error: {str(e)}"}), 400
        
    #? DELETE
    @app.route("/books/<int:book_id>", methods=["DELETE"])
    def delete_books(book_id):
        book = handle_books.get_book_by_id(book_id)
        if not book:
            return jsonify({"error": f"Error: book not found"}), 400

        try:
            handle_books.delete_book(book_id)
            return jsonify({"message": f"Book '{book['title']}' deleted!"})
        except Exception as e:
            return jsonify({"error": f"Error: {str(e)}"}), 500
        

    #! DATA RELATION ROUTES
    #? GET
    @app.route("/data", methods=["GET"])
    def index():
        data = handle_books_authors.get_data()
        return jsonify(data)
    
    @app.route("/data/book/<int:book_id>", methods=["GET"])
    def get_data_by_book_id(book_id):
        data = handle_books_authors.get_data_by_book_id(book_id)
        return jsonify(data)
    
    @app.route("/data/author/<int:author_id>", methods=["GET"])
    def get_data_by_author_id(author_id):
        data = handle_books_authors.get_data_by_author_id(author_id)
        return jsonify(data)

    #? POST
    @app.route("/data", methods=["POST"])
    def add_data():
        data = request.get_json()
        book_id = data["book_id"]
        author_id = data["author_id"]

        try:
            handle_books_authors.add_data(book_id, author_id)
            return jsonify({"message": f"Data added!"}), 201
        except Exception as e:
            return jsonify({"error": f"Error: {e}"}), 400
        
    #? DELETE
    @app.route("/data/<int:book_id>/<int:author_id>", methods=["DELETE"])
    def delete_data(book_id, author_id):
        try:
            handle_books_authors.delete_data(book_id, author_id)
            return jsonify({"message": "Data deleted successfully!"}), 200
        except Exception as e:
            return jsonify({"error": f"Error: {str(e)}"}), 500

    """  @app.route("/")
    def index():
        with sqlite3.connect("management.db") as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM book_authors")
            rows = cursor.fetchall()
            return jsonify(rows)"""
