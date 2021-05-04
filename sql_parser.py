import sqlite3


class SQLParser:
    def __init__(self):
        self.bd_name = 'orders.db'
        self.table = 'orders'
        conn = sqlite3.connect(self.bd_name)
        cur = conn.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS """ + self.table + """ (
           userid INT,
           date TEXT,
           currency1 TEXT,
           currency2 TEXT,
           value FLOAT);
        """)
        conn.commit()
        conn.close()

    def get_all(self, user_id, columns=('date', 'currency1', 'currency2', 'value')):
        conn = sqlite3.connect(self.bd_name)
        cur = conn.cursor()
        output = []
        columns_names = ' ,'.join(columns)
        for num in range(len(columns)):
            output.append([i[num] for i in cur.execute(f"SELECT {columns_names} "
                                                       f"FROM {self.table} WHERE "
                                                       f"userid = '{user_id}'")])
        conn.close()
        return output

    def add(self, data):
        conn = sqlite3.connect(self.bd_name)
        cur = conn.cursor()
        cur.execute("INSERT INTO " + self.table + " VALUES(?, ?, ?, ?, ?);", data)
        conn.commit()
        conn.close()
