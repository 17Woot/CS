import sqlite3
import myvalidation_classwork

class Db_hw():
    def __init__(self):
        self.valid = myvalidation_classwork.Validator()

    def createTable(self):
        try:
            self.connect = sqlite3.connect("hwlog.db")
            self.connect.execute('''CREATE TABLE IF NOT EXISTS WORK 
                           (ID INTEGER PRIMARY KEY NOT NULL,
                            Homework      CHAR(15)    NOT NULL,
                            Subject      CHAR(10)    NOT NULL,
                            Due_Date      DATE    NOT NULL
                            );''')
            self.connect.commit()
            self.connect.close()
            return True
        except Exception as e:
            print(e)
            return False

    def insertData(self, id, givenHomework, givenSubject, givenDue_Date):
        try:
            self.connect = sqlite3.connect("hwlog.db")
            self.connect.execute('''insert into WORK  (ID,Homework, Subject, Due_Date) values (?, ?, ?, ?)''',
                         (id, givenHomework, givenSubject, givenDue_Date))
            self.connect.commit()
            self.connect.close()
            return True
        except Exception as e:
            print(e)
            return False



    def showAllRecords(self):
        try:
            self.connect = sqlite3.connect("hwlog.db")
            cursor = self.connect.execute(''' SELECT ID, Homework, Subject, Due_Date FROM  USERS ''')
            for row in cursor:
                print("Homework = ", row[0])
                print("Subject = ", row[1])
                print("Due_Date = ", row[2], "\n")
                return True
        except:
            return False

    def deleteRecord(self, id):
        try:
            self.connect = sqlite3.connect("hwlog.db")
            self.connect.execute('''delete from USERS where ID = ?''', (id,))
            self.connect.commit()
            self.connect.close()
            return True
        except:
            return False

    def search_by_date(self, givenDue_Date):
        try:
            self.connect = sqlite3.connect("hwlog.db")
            cursor = self.connect.execute(''' SELECT ID, Homework, Subject, Due_Date FROM  WORK WHERE Due_Date = ?''', (givenDue_Date,))
            SEARCH = "SELECT * FROM WORK WHERE Due_Date = ?"
            cursor.execute(SEARCH, (givenDue_Date,))
            rows = cursor.fetchall()
            for row in rows:
                print(row)
            return True
        except Exception as e:
            print(e)





if __name__ == "__main__":
    log = Db_hw()
    log.createTable()
    log.insertData(7,"r and j", "english", "12/12/1212")
    log.insertData(8,"r and j", "english", "12/12/1212")
    log.search_by_date("12/12/1212")