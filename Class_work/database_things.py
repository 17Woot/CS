import sqlite3
class Database():
    def __init__(self):
        pass

    def createTable(self):
        try:
            self.connect = sqlite3.connect("test_database.db")
            self.connect.execute('''CREATE TABLE IF NOT EXISTS USERS 
                           (ID INTEGER PRIMARY KEY NOT NULL,
                            UserName      TEXT    NOT NULL,
                            password      TEXT    NOT NULL
                            );''')
            self.connect.commit()
            self.connect.close()
            return True
        except:
            return False

    def insertData(self, id, givenUser, givenPassword):
        try:
            self.connect = sqlite3.connect("test_database.db")
            self.connect.execute('''insert into USERS  (ID,UserName, password) values (?, ?, ?)''',
                         (id, givenUser, givenPassword))
            self.connect.commit()
            self.connect.close()
            return True
        except:
            return False

    def showAllRecords(self):
        try:
            self.connect = sqlite3.connect("test_database.db")
            cursor = self.connect.execute(''' SELECT ID, UserName, password FROM  USERS ''')
            for row in cursor:
                print("User Name = ", row[0])
                print("Passwords = ", row[1], "\n")
                return True
        except:
            return False

    def deleteRecord(self, id):
        try:
            self.connect = sqlite3.connect("test_database.db")
            self.connect.execute('''delete from USERS where ID = ?''', (id,))
            self.connect.commit()
            self.connect.close()
            return True
        except:
            return False





if __name__ == "__main__":
    db = Database()
    db.createTable()
    for i in range(1001,2001):
        db.insertData(i, "User"+str(i), "Password"+str(i))









