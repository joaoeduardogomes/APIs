from flask import Flask, jsonify, request, redirect, url_for
import sqlite3
import handle_authors

app = Flask(__name__)

@app.route("/")
def index():
    with sqlite3.connect("management.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM book_authors")
        rows = cursor.fetchall()
        return jsonify(rows)
    
@app.route("/authors", methods=["GET"])
def get_authors():
    authors = handle_authors.get_authors()
    return jsonify(authors)

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


def sync_db():
    with sqlite3.connect("management.db") as conn:
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS authors (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                firstname TEXT NOT NULL,
                lastname TEXT NOT NULL
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                author_id INTEGER,
                FOREIGN KEY (author_id) REFERENCES authors (id) ON DELETE CASCADE
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS book_authors (
                book_id INTEGER NOT NULL,
                author_id INTEGER NOT NULL,
                PRIMARY KEY (book_id, author_id),
                FOREIGN KEY (book_id) REFERENCES books (id) ON DELETE CASCADE,
                FOREIGN KEY (author_id) REFERENCES authors (id) ON DELETE CASCADE
            )
        """)

        conn.commit()


if __name__ == "__main__":
    sync_db()
    app.run(debug=True)
