import mysql.connector


class DBmanager:
    def __init__(self, database):
        self.config = {
            "host": "127.0.0.1",
            "port": 3306,
            "user": "root",
            "password": "secret",
            "database": "mydb",
        }

    def get_connection(self):
        try:
            conn = mysql.connector.connect(self.config)
            return conn
        except Exception as e:
            print(e)

    def create_book_table(self):
        self.db = self.get_connection()
        cursor = self.db.cursor()
        cursor.execute("""CREATE TABLE if NOT EXSIST books(
                            id INT AUTO_INCREMENT PRIMARY KEY,
                            title VARCHAR(50) NOT NULL,
                            auther VARCHAR(50) NOT NULL,
                            genre VARCHAR(50) NOT NULL ENUM("Fiction", "Non-Fiction", "Science", "History", "Other"),
                            is_available BOOLEAN NOT NULL,
                            borrowed_by_member_id INT DEFAULT null
                            )
                            """)
        cursor.close()

    def create_members_table(self):
        self.db = self.db.cursor
        cursor = self.db.cursor()
        cursor.execute("""CREATE TABLE if NOT EXSIST members(
                            id INT AUTO_INCREMENT PRIMARY KEY,
                            name VARCHAR(50) NOT NULL,
                            email VARCHAR(50) NOT NULL UNIQUE,
                            is_active BOOLEAN NOT NULL,
                            total_borrowed INT AUTO_INCREMENT
                            )
                            """)
        cursor.close()