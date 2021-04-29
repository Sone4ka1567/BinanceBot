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

    def get_all(self):
        pass

    def add(self, data):
        conn = sqlite3.connect(self.bd_name)
        cur = conn.cursor()
        cur.execute("INSERT INTO orders VALUES(?, ?, ?, ?, ?);", data)
        conn.commit()
