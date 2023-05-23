import sqlite3

def cSt():
    db = "./students.db"
    conn = sqlite3.connect(db)
    c = conn.cursor()
    cmd = "CREATE TABLE IF NOT EXISTS students (Name TEXT, Age INT)"
    c.execute(cmd)
    data = [("Robert", 10), ("Sally", 15), ("Matthew", 7)]
    c.executemany("INSERT INTO students VALUES (?, ?)", data)
    conn.commit()
    print("students table created and 3 records added")

def show_single_record():
    db = "./students.db"
    conn = sqlite3.connect(db)
    c = conn.cursor()
    varname = input("Enter name of student to show: ")
    sqlstrong = "SELECT * from students WHERE Name = '%s'" % varname
    c.execute(sqlstrong)
    result = c.fetchall()
    print(result)
    conn.close()




if __name__ == "__main__":
    show_single_record()