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
        raise RuntimeError(f"Database error: {e}")