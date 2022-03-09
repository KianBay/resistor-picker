import sqlite3

from resistor_pick import RESISTORS

class db():
    def __init__(self):

        self.conn = sqlite3.connect('resistors.db')
        self.cur = self.conn.cursor()
        

    def setup(self):
        self.cur.execute("CREATE TABLE lab_resistors (resistor_id INTEGER PRIMARY KEY AUTOINCREMENT, resistance_value FLOAT)")

    def add_lab_res(self):
        for res in RESISTORS:
            self.cur.execute("INSERT INTO lab_resistors(resistance_value) VALUES(?)",(res,))
            self.conn.commit()

if __name__ == '__main__':
    newdb = db()
    newdb.setup()
    newdb.add_lab_res()