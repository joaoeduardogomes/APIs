from flask import Flask, request, jsonify
import sqlite3
import handle_authors


def register_routes(app):

    #! GET
    @app.route("/authors", methods=["GET"])
    def get_authors():
        authors = handle_authors.get_authors()
        return jsonify(authors)

    #! GET
    @app.route("/authors/name/<string:name>", methods=["GET"])
    def get_author_by_name(name):
        author = handle_authors.get_author_by_name(name)
        return jsonify(author)

    #! GET
    @app.route("/authors/name", methods=["GET"])
    def list_authors_names():
        names = handle_authors.list_authors_names()
        return {"names": (names)}

    #! GET
    @app.route("/authors/country/<string:country>", methods=["GET"])
    def get_country_authors(country):
        authors = handle_authors.get_country_authors(country)
        return jsonify(authors)

    #! GET
    @app.route("/authors/country", methods=["GET"])
    def list_authors_countries():
        countries = handle_authors.list_authors_countries()
        return {"countries": (countries)}

    #! POST
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

    #! GET
    @app.route("/authors/<int:author_id>", methods=["GET"])
    def get_author_by_id(author_id):
        author = handle_authors.get_author_by_id(author_id)
        if not author:
            return jsonify({"error": f"Error: author not found"}), 400

        author = handle_authors.get_author_by_id(author_id)
        return jsonify(author)

    #! PUT
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

    #! DELETE
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

    """  @app.route("/")
    def index():
        with sqlite3.connect("management.db") as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM book_authors")
            rows = cursor.fetchall()
            return jsonify(rows)"""
