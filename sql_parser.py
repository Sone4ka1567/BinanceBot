import sqlite3


class SQLParser:
    def __init__(self):
        self.bd_name = 'orders.db'
        conn = sqlite3.connect(self.bd_name)
        cur = conn.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS orders(
           userid INT PRIMARY KEY,
           date TEXT,
           currency1 TEXT,
           currency2 TEXT,
           value FLOAT);
        """)
        conn.commit()
