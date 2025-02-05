from flask import Flask, jsonify, request, redirect, url_for
import sqlite3
import routes

app = Flask(__name__)

routes.register_routes(app)


def sync_db():
        with sqlite3.connect("management.db") as conn:
            cursor = conn.cursor()
            cursor.execute("PRAGMA foreign_keys = ON;")

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS authors (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    country TEXT
                )
            """)
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS books (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    genre TEXT NOT NULL,
                    isbn TEXT UNIQUE,
                    released_year INTEGER NOT NULL CHECK(released_year >= 1500)
                )
            """)
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS books_authors (
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
