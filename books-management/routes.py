from flask import Flask, request, jsonify
import sqlite3
import handle_authors  

def register_routes(app):

    #! GET
    @app.route("/authors", methods=["GET"])
    def get_authors():
        authors = handle_authors.get_authors()
        return jsonify(authors)

    #! POST
    @app.route("/authors", methods=["POST"])
    def add_author():
        data = request.get_json()
        firstname = data["firstname"]
        lastname = data["lastname"]
        
        try:
            handle_authors.register_author(firstname, lastname)
            return jsonify({"message": f"Author: {firstname} {lastname} registered!"}), 201
        except Exception as e:
            return jsonify({"error": f"Error: {e}"}), 400

    #! GET
    @app.route("/authors/<int:author_id>", methods=["GET"])
    def get_author_by_id(author_id):
        author = handle_authors.get_author_by_id(author_id)
        return jsonify(author)
    
    #! PUT
    @app.route("/authors/<int:author_id>", methods=["PUT"])
    def update_author(author_id):
        data = request.get_json()
        firstname = data["firstname"]
        lastname = data["lastname"]
        
        try:
            updated_author = handle_authors.update_author(author_id, firstname, lastname)
            return jsonify(updated_author)
        except Exception as e:
            return jsonify({"error": f"Error: {e}"}), 400

    """  @app.route("/")
    def index():
        with sqlite3.connect("management.db") as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM book_authors")
            rows = cursor.fetchall()
            return jsonify(rows)"""