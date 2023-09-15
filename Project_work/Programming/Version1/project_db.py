import sqlite3
from tkinter import messagebox

class CLS_db():
    def __init__(self):
        self.mt_createTable()
        self.mt_add_user("admin", "admin")


    def mt_createTable(self):
        try:
            conn = sqlite3.connect('accounts.db')
            conn.execute('''CREATE TABLE USERS
            (UserName TEXT PRIMARY KEY NOT NULL,
            password TEXT NOT NULL);''')
            conn.commit()
            conn.close()
            return True
        except:
            return False
        
    def mt_add_user(self, givenUser, givenPassword):
        try:
            if self.mt_user_exists() == True:
                return False
            else:
                conn = sqlite3.connect('accounts.db')
                conn.execute('''insert into USERS  (UserName, password) values (?, ?)''',
                             (givenUser, givenPassword))
                conn.commit()
                conn.close()
                return True
        except:
            return False

    def mt_user_exists(self, givenUser):

        try:
            conn = sqlite3.connect('accounts.db')
            cursor = conn.execute(''' SELECT UserName FROM  USERS ''')
            for row in cursor:
                if row[0] == givenUser:
                    return True
                else:
                    pass
        except Exception as e:
            print(e)
            return False

    def mt_password_correct(self, givenUser, givenPassword):
        found = False
        try:
            conn = sqlite3.connect('accounts.db')
            cursor = conn.execute(''' SELECT UserName, password FROM  USERS ''')
            for row in cursor:
                if row[0] == givenUser and row[1] == givenPassword:
                    found = True
                else:
                    pass
            return found
        except:
            return False

    def mt_isadmin(self, givenUser):
        try:
            conn = sqlite3.connect('accounts.db')
            cursor = conn.execute(''' SELECT UserName, password FROM  USERS ''')
            for row in cursor:
                if row[0] == givenUser and row[1] == "admin":
                    return True
                else:
                    return False
        except:
            return False

    def mt_delete_user(self, givenUser):
        try:
            conn = sqlite3.connect('accounts.db')
            conn.execute('''DELETE FROM USERS WHERE UserName = ?''', (givenUser,))
            conn.commit()
            conn.close()
            return True
        except:
            return False


