# import sqlite3

# conn = sqlite3.connect("database.db")
# print("Connected to database successfully")

# def create_table():
#     conn.execute('CREATE TABLE ZodiacInfo ( ZodiacSign TEXT, Planet TEXT, Date DATE, Seat TEXT);')
#     conn.close()
    
# def insert_into():
#     conn = sqlite3.connect('database.db')
#     cursor = conn.cursor()

#     cursor.execute('''
#         INSERT INTO ZodiacInfo (ZodiacSign)
#         VALUES (?);
#     ''', ('Alice',))
    
#     conn.commit()
#     conn.close()

# if __name__ == "__main__": 
#     insert_into()