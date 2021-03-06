import sqlite3

from resistor_pick import RESISTORS

class db():
    def __init__(self):

        self.conn = sqlite3.connect('resistors.db') #Also creates the db file if none present
        self.cur = self.conn.cursor()
        

    def setup(self):
        self.cur.execute("CREATE TABLE lab_resistors (resistor_id INTEGER PRIMARY KEY AUTOINCREMENT, resistance_value FLOAT)")

    def add_lab_res(self):
        try:
            for res in RESISTORS:
                self.cur.execute("INSERT INTO lab_resistors(resistance_value) VALUES(?)",(res,))
                self.conn.commit()
        except sqlite3.OperationalError as e: #We run the setup if table doesn't exist yet
            self.setup()

    def get_lab_res(self):
        try:
            self.cur.execute("SELECT resistance_value FROM lab_resistors")
            data = self.cur.fetchall()
            lst = []
            for entries in data:
                lst.append(entries[0])
                #lst.sort(reverse=True)
            return lst
            
        except sqlite3.OperationalError as e:
            self.setup()
            self.add_lab_res()
            self.cur.execute("SELECT resistance_value FROM lab_resistors")
            data = self.cur.fetchall()
            lst = []
            for entries in data:
                lst.append(entries[0])
                #lst.sort(reverse=True)
            return lst
        

        


if __name__ == '__main__':
    newdb = db()
    newdb.setup()
    newdb.add_lab_res()
    #print(newdb.get_lab_res())