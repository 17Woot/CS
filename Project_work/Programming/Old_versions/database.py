################################################
# name: Reece Wootley                          #
# date: 12/05/2023                             #
# user database module using sql               #
################################################
import sqlite3
class Db(object):
    # _____________ method to create tables _________________________________
    def create_table(self):
        try:
            conn = sqlite3.connect('../Version1/accounts.db')
            # print("Opened database successfully")

            conn.execute('''CREATE TABLE IF NOT EXISTS USERS 
                           (UserName      TEXT     PRIMARY KEY     NOT NULL,
                            password      TEXT    NOT NULL )''')

            # print("Users Accounts Table is created successfully")
            conn.close()
            self.add_user("admin", "admin")
            return True
        except:
            return False

    # _____________ method to insert data into the table _________________________________
    def add_user(self, givenUser, givenPassword):
        try:
            if self.user_exists(givenUser) == True:
                return False
            else:
                conn = sqlite3.connect('../Version1/accounts.db')
                # insert data into database table
                conn.execute('''insert into USERS  (UserName, password) values (?, ?)''',
                             (givenUser, givenPassword))
                conn.commit()  # do not forget to commit the data (i.e. save the data on the table
                conn.close()
                return True
        except:
            return False
        
    
    # _____________ method to check if user exists _________________________________
    def user_exists(self, givenUser):
        try:
            conn = sqlite3.connect('../Version1/accounts.db')
            cursor = conn.execute(''' SELECT UserName, password FROM  USERS ''')
            for row in cursor:
                if row[0] == givenUser:
                    return True
                else:
                    return False
        except:
            return False
       

    # ------------- method to check if password is correct ------------------------
    def password_correct(self, givenUser, givenPassword):
        try:
            conn = sqlite3.connect('../Version1/accounts.db')
            cursor = conn.execute(''' SELECT UserName, password FROM  USERS ''')
            for row in cursor:
                if row[0] == givenUser and row[1] == givenPassword:
                    return True
                else:
                    return False
        except:
            return False

    # ------------ method to check if user is admin -------------------------------
    def is_admin(self, givenUser):
        try:
            conn = sqlite3.connect('../Version1/accounts.db')
            cursor = conn.execute(''' SELECT UserName, password FROM  USERS ''')
            for row in cursor:
                if row[0] == givenUser and row[1] == "admin":
                    return True
                else:
                    return False
        except:
            return False



    # _____________ method to show all records stored in the table tables _________________________________

    def showAllRecords(self):
        try:
            conn = sqlite3.connect('../Version1/accounts.db')
            # Select all records in a table:
            cursor = conn.execute(''' SELECT UserName, password FROM  USERS ''')

            for row in cursor:
                print("User Name = ", row[0])
                print("Passwords = ", row[1], "\n")
                return True
        except:
            return False

    # _____________ method to delete a record from the table _________________________________
    def deleteRecord(self, givenuser):
        try:
            conn = sqlite3.connect('../Version1/accounts.db')
            conn.execute("DELETE FROM USERS WHERE  UserName =?", (givenuser,))
            print("deleted")
            conn.commit()
            conn.close()
            return True
        except:
            return False


    # _____________ method to Update password _________________________________
    def updatePassword(self, givenUser, newPassword):
        try:
            conn = sqlite3.connect('../Version1/accounts.db')
            conn.execute('''UPDATE USERS  SET password = ? WHERE UserName = ? ''', (newPassword, givenUser))
            conn.commit()
            conn.close()
        except:
            return False

    # _____________ method to search for a user  _________________________________
    def searchUser(self, givenUser, givenpassword):
        conn = sqlite3.connect('../Version1/accounts.db')
        # Select all records in a table:
        cursor = conn.execute(''' SELECT UserName, password FROM  USERS ''')
        for row in cursor:
            if row[0] == givenUser and row[1] == givenpassword:
                return True
        return False

    # _____________ method to create table dictionary _________________________________
    def createDictionary(self):
        try:
            conn = sqlite3.connect('../Version1/accounts.db')
            cursor = conn.execute('select * from USERS')  # you can change the table name to view the columns
            columns = cursor.description
            colnames = cursor.description  # Gets columns names
            print("You have created a table with the following columns:")
            for row in colnames:
                print(row[0])
            return True
        except:
            return False

    # ______________  TESTING ALL ABOVE _________________________

if __name__ == "__main__":
    pass














