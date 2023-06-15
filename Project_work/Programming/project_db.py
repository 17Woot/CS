import sqlite3

class CLS_db():
    def __init__(self):
        pass 

    def mt_createTable(self):
        try:
            conn = sqlite3.connect('accounts.db')
            conn.execute('''CREATE TABLE USERS
            (UserName TEXT PRIMARY KEY NOT NULL,
            password TEXT NOT NULL);''')
            conn.commit()
            conn.close()
            self.add_user("admin", "admin")
            return True
        except:
            return False
        
    def mt_add_user(self, givenUser, givenPassword):
        try:
            if self.user_exists(givenUser) == True:
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
            cursor = conn.execute(''' SELECT UserName, password FROM  USERS ''')
            for row in cursor:
                if row[0] == givenUser:
                    return True
                else:
                    return False
        except:
            return False
        
    def mt_password_correct(self, givenUser, givenPassword):
        try:
            conn = sqlite3.connect('accounts.db')
            cursor = conn.execute(''' SELECT UserName, password FROM  USERS ''')
            for row in cursor:
                if row[0] == givenUser and row[1] == givenPassword:
                    return True
                else:
                    return False
        except:
            return False
