import sqlite3

conn = sqlite3.connect("akhss.db") 

c = conn.cursor()

c.execute("""
            CREATE TABLE IF NOT EXISTS student 
            (   id INTEGER PRIMARY KEY AUTOINCREMENT,
                std_name TEXT NOT NULL,
                std_father TEXT NOT NULL,
                std_mother TEXT NOT NULL,
                std_batch  TEXT NOT NULL,
                std_roll_no INTEGER NOT NULL,
                Std_class TEXT NOT NULL,
                std_section TEXT NOT NULL,
                std_dob TEXT NOT NULL,
                std_gender TEXT NOT NULL,
                std_phone NUMBER NOT NULL,
                std_email TEXT NOT NULL,
                std_address TEXT NOT NULL  
            )
""")
c.execute("""
            CREATE TABLE IF NOT EXISTS techer 
            (   id INTEGER PRIMARY KEY AUTOINCREMENT,
                tech_name TEXT NOT NULL,
                tech_email TEXT NOT NULL,
                tech_phone NUMBER NOT NULL,
                tech_gender TEXT NOT NULL,
                tech_subject TEXT NOT NULL,
                tech_address TEXT NOT NULL
            )
                
""")

conn.commit()
conn.close()