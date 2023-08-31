import sqlite3

conn = sqlite3.connect("akhss.db") 

c = conn.cursor()

c.execute("""
            CREATE TABLE IF NOT EXISTS student
           
            (   std_id INTEGER PRIMARY KEY,
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
                std_address TEXT NOT NULL,  
            FOREIGN KEY (std_class) REFERENCES class (class_id) 
            FOREIGN KEY (std_section) REFERENCES section (section_id)
            )
""")
c.execute("""
            CREATE TABLE IF NOT EXISTS teacher
           
            (   teach_id INTEGER PRIMARY KEY,
                teach_name TEXT NOT NULL,
                teach_email TEXT NOT NULL,
                teach_phone NUMBER NOT NULL,
                teach_gender TEXT NOT NULL,
                teach_subject TEXT NOT NULL,
                teach_address TEXT NOT NULL,
            FOREIGN KEY (teach_subject) REFERENCES subject (subject_id)
            )
                
""")
c.execute("""
            CREATE TABLE IF NOT EXISTS subject
          
            (   subject_id INTEGER PRIMARY KEY AUTOINCREMENT,
                subject_name TEXT NOT NULL
            ) 
              
""")
c.execute("""
            CREATE TABLE IF NOT EXISTS class
          
            (   class_id INTEGER PRIMARY KEY AUTOINCREMENT,
                class_name TEXT NOT NULL
            )
          
""")
c.execute("""
            CREATE TABLE IF NOT EXISTS section
          
            (   section_id INTEGER PRIMARY KEY AUTOINCREMENT,
                section_name TEXT NOT NULL
            )
          
""")
c.execute("""
            CREATE TABLE IF NOT EXISTS result
          
            (   result_id INTEGER PRIMARY KEY AUTOINCREMENT,
                std_id INTEGER NOT NULL,
                subject_id INTEGER NOT NULL,
                class_id INTEGER NOT NULL,
                section_id INTEGER NOT NULL,
                obt_marks   INTEGER NOT NULL,
                t_marks INTEGER NOT NULL,
                percentage INTEGER NOT NULL,
                rank INTEGER NOT NULL,
            FOREIGN KEY (std_id) REFERENCES student (std_id)
            FOREIGN KEY (subject_id) REFERENCES subject (subject_id)
            FOREIGN KEY (class_id) REFERENCES class (class_id)
            FOREIGN KEY (section_id) REFERENCES section (section_id)
            )
          
""")
c.execute("""
            CREATE TABLE IF NOT EXISTS home_work
            
            (   hw_id INTEGER PRIMARY KEY AUTOINCREMENT,
                hw_subject TEXT NOT NULL,
                hw_assign_date TEXT NOT NULL,
                hw_deadline TEXT NOT NULL,
                hw_description TEXT NOT NULL,
                hw_marks INTEGER NOT NULL,
            FOREIGN KEY (hw_subject) REFERENCES subject (subject_id)
            )
""")
c.execute("""
            CREATE TABLE IF NOT EXISTS volitions 
          
            (   vol_id INTEGER PRIMARY KEY AUTOINCREMENT,
                vol_type TEXT NOT NULL,
                vol_date_time TEXT NOT NULL,
                vol_description TEXT NOT NULL,
                vol_reported_by TEXT NOT NULL,
            FOREIGN KEY (vol_reported_by) REFERENCES teacher (teach_id) 
            )
""")
c.execute("""
            CREATE TABLE IF NOT EXISTS activity
          
            (   activity_id INTEGER PRIMARY KEY AUTOINCREMENT, 
                activity_type TEXT NOT NULL,
                activity_head_by TEXT NOT NULL,
                activity_description TEXT NOT NULL,
            FOREIGN KEY (activity_head_by) REFERENCES teacher (teach_id)
            )
""")
c.execute("""
            CREATE TABLE IF NOT EXISTS club
           
            (   club_id INTEGER PRIMARY KEY AUTOINCREMENT,
                club_name TEXT NOT NULL,
                club_teacher TEXT NOT NULL,
                club_head TEXT NOT NULL,
            FOREIGN KEY (club_teacher) REFERENCES teacher (teach_id)
            FOREIGN KEY (club_head) REFERENCES student (std_id)
            )
""")
conn.commit()
conn.close()