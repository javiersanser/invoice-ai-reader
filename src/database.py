# SQLite database management & schemas
# In production it should use a more secure method like SQLAlchemy. 
# This is just for demonstration purposes.

from os import close
import sqlite3
from config import DB_PATH

def connect_db():
    try:
        conn = sqlite3.connect(DB_PATH)
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        return None
    return conn  # Return the database connection, be sure to close it after using this function.

def initialize_db():
    conn = None
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS invoices(
            id INTEGER PRIMARY KEY,
            file_name TEXT NOT NULL,
            file_path TEXT NOT NULL,
            status TEXT DEFAULT 'pending' CHECK (status IN ('pending', 'completed', 'error')),
            date TEXT,
            tax_id TEXT,
            vendor_name TEXT,
            invoice_concept TEXT,
            base_amount REAL,
            vat_pct REAL,
            vat_amount REAL,
            total_amount REAL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
                       
    except sqlite3.Error as e:
        print(f"Error initializing database: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    initialize_db()
