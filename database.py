import sqlite3
from datetime import datetime

DB_PATH = "prices.db"


def init_db(path: str = DB_PATH):
    conn = sqlite3.connect(path)
    cur = conn.cursor()
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS prices (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product TEXT NOT NULL,
            price REAL NOT NULL,
            timestamp DATETIME NOT NULL
        );
    """
    )
    conn.commit()
    conn.close()


def insert_price(product: str, price: float, timestamp: datetime, path: str = DB_PATH):
    conn = sqlite3.connect(path)
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO prices (product, price, timestamp) VALUES (?, ?, ?)",
        (product, price, timestamp),
    )
    conn.commit()
    conn.close()


def get_history(product: str, path: str = DB_PATH) -> list:
    conn = sqlite3.connect(path)
    cur = conn.cursor()
    cur.execute(
        "SELECT price, timestamp FROM prices WHERE product = ? ORDER BY timestamp",
        (product,),
    )
    rows = cur.fetchall()
    conn.close()
    return rows
