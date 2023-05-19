import sqlite3

class Db_bikes():
    def __init__(self):
        pass

    def create_table_bike(self):
        try:
            conn = sqlite3.connect("bikes.db")
            print("Opened DB Successfully")
            conn.execute('''CREATE TABLE IF NOT EXISTS BIKES
                         (BIKE        INT PRIMARY KEY NOT NULL,
                         CUSTOMER_ID  INT             NOT NULL,
                         DATE         DATE            NOT NULL,
                         FOREIGN KEY(CUSTOMER_ID) REFERENCES CUSTOMERS(CUSTOMER_ID));''')
            print("BIKE TABLE CREATED")
            conn.close()
        except Exception as e:
            print(e)
            return False

    def create_table_customer(self):
        try:
            conn = sqlite3.connect("bikes.db")
            print("Opened DB Successfully")
            conn.execute('''CREATE TABLE IF NOT EXISTS CUSTOMERS
                            (CUSTOMER_ID INT PRIMARY KEY  NOT NULL,
                             NAME         TEXT            NOT NULL,
                             PHONE_NO    INT              NOT NULL
                             );''')
            print("CUSTOMERS TABLE CREATED")
            conn.close()
        except Exception as e:
            print(e)
            return False


    def add_bike(self, bike_no, customer_id, date):
        try:
            conn = sqlite3.connect("bikes.db")
            conn.execute('''insert into BIKES  (BIKE) values (?)''', (bike_no))
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            print(e)
            return False

    def add_customer(self, customer_id, name, phone_no):
        try:
            conn = sqlite3.connect("bikes.db")
            conn.execute('''insert into CUSTOMERS  (CUSTOMER_ID, NAME, PHONE_NO) values (?, ?, ?)''',
                         (customer_id, name, phone_no))
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            print(e)
            return False

    def book_a_bike(self):
        pass

    def update_Customer_details(self):
        pass

    def display_bookings(self):
        try:
            conn = sqlite3.connect("bikes.db")
            cursor = conn.execute(''' SELECT BIKE, CUSTOMER_ID FROM  BIKES ''')
            for row in cursor:
                print("Bike = ", row[0])
                print("Customer ID = ", row[1], "\n")
                return True
        except Exception as e:
            print(e)
            return False


if __name__ == "__main__":
    db = Db_bikes()
    db.create_table_bike()
    db.create_table_customer()
    db.add_bike("1","1","19/05/2023")






