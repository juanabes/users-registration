import sqlite3
from sqlite3 import Error

class Database:
    """
    Create a connection with the database an create the tables inside it if isn't exists
    """
    def __init__(self, db_name="database.db"):
        self.db_name = db_name
        
    def get_connection(self):
        """Get the connection to the database and return it"""
        try:
            return sqlite3.connect(self.db_name)
        except Error as e:
            print(f"Can't connect to the database: {str(e)}")
            return False
    # End of get_connection
    
    def create_tables(self):
        """Create table into the database if this not exists"""
        conexion = self.get_connection()
        if conexion is None:
            return False
        
        try:
            with conexion:
                cursor = conexion.cursor()
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS person(
                        identity_document VARCHAR(11) PRIMARY KEY,
                        name VARCHAR(20) NOT NULL,
                        surname VARCHAR(20) NOT NULL,
                        address VARCHAR(100),
                        phone_number VARCHAR(11)
                    )
                """)
                conexion.commit()
                return True
        except Error as e:
            print(f"An error occurred while try connecting with the database: {str(e)}")
            return False
    # End of create_tables