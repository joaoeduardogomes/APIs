# Book Management API

A simple RESTful API for managing books and authors using Flask and SQLite.

## Features

- Add, retrieve, update, and delete authors.

- Add, retrieve, update, and delete books.

- Associate books with authors.

- Retrieve all books by a specific author.

## Technologies Used

- ![Python](https://img.shields.io/badge/PYTHON-%20?style=for-the-badge&logo=python&logoColor=white&color=%23356F9F)

- ![Static Badge](https://img.shields.io/badge/flask-%232A2123?style=for-the-badge&logo=flask)

- SQLite

## Installation

### Prerequisites

- Python 3 installed on your system

- `pip` installed for package management

### Setup

1. Clone the repository:
   
   ```
   git clone https://github.com/yourusername/book-management-api.gitcd book-management-api
   ```

2. Create a virtual environment (optional but recommended):
   
   ```
   python3 -m venv venvsource venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:
   
   ```
   pip install -r requirements.txt
   ```

4. Initialize the database:
   
   ```
   python sync_db.py
   ```

5. Run the application:
   
   ```
   python app.py
   ```

## API Endpoints

### **Authors**

- **GET** `/authors` - Retrieve all authors

- **GET** `/authors/<id>` - Retrieve a specific author by ID

- **POST** `/authors` - Add a new author (requires `name` and `country` in JSON payload)

- **PUT** `/authors/<id>` - Update an author's details

- **DELETE** `/authors/<id>` - Remove an author

### **Books**

- **GET** `/books` - Retrieve all books

- **GET** `/books/<id>` - Retrieve a specific book by ID

- **GET** `/books/title/<title>` - Retrieve a book by title

- **POST** `/books` - Add a new book (requires `title`, `year`, and `author_id` in JSON payload)

- **PUT** `/books/<id>` - Update a book's details

- **DELETE** `/books/<id>` - Remove a book

### **Book-Author Association**

- **GET** `/authors/<id>/books` - Retrieve all books by a specific author

## Example Request

### Add a New Author

```
curl -X POST http://127.0.0.1:5000/authors \     -H "Content-Type: application/json" \     -d '{"name": "J.K. Rowling", "country": "UK"}'
```

### Add a New Book

```
curl -X POST http://127.0.0.1:5000/books \     -H "Content-Type: application/json" \     -d '{"title": "Harry Potter and the Philosopher's Stone", "year": 1997, "author_id": 1}'
```

## Error Handling

The API returns JSON responses for errors with relevant HTTP status codes, such as:

- `400 Bad Request` for invalid input.

- `404 Not Found` for missing resources.

- `500 Internal Server Error` for unexpected issues.

## Contributing

Feel free to fork this repository, create a feature branch, and submit a pull request.

## License

This project is open-source under the MIT License.
