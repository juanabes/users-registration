from model.database import Database
from sqlite3 import IntegrityError, Error

class PersonModel:
    """Create sentencies SQL to manipulate person data"""
    def __init__(self, db: Database):
        self.db = db
        
    def add_person(self, person_data:tuple) -> bool:
        """Add a new person into the database"""
        with self.db.get_connection() as connection:
            try:
                cursor = connection.cursor()
                cursor.execute("""
                    INSERT INTO person(identity_document, name, surname, address, phone_number) 
                    VALUES (?, ?, ?, ?, ?) 
                """, person_data)
                connection.commit()
                return True
            except IntegrityError as e:
                print(f"Error: Person with ID '{person_data[0]}' already exists or a constraint was violated: {str(e)}")
                return False
            except Error as e:
                print(f"Error: an error occurred while adding person data: {str(e)}")
                return False
    # End of add_person
    
    def read_person(self, identity_document: str) -> tuple | None:
        """Read the person data from the database by identity document"""
        with self.db.get_connection() as connection:
            try:
                cursor = connection.cursor()
                cursor.execute("SELECT * FROM person WHERE identity_document=?", (identity_document,))
                person_data = cursor.fetchone()
                return person_data
            except Error as e:
                print(f"Error: can't read the person data from the database: {str(e)}")
                return None
    # End of read_person
    
    def read_all_persons(self):
        """Read all person data from the database"""
        with self.db.get_connection() as connection:
            try:
                cursor = connection.cursor()
                cursor.execute("SELECT * FROM person")
                all_persons = cursor.fetchall()
                return all_persons
            except Error as e:
                print(f"Error: an error occurred while reading all persons from the database: {str(e)}")
                return []
    # End of read_all_persons
    
    def update_person(self, person_data: tuple) -> bool:
        """Update the person data into the database by identity document"""
        with self.db.get_connection() as connection: 
            try:
                cursor = connection.cursor()
                cursor.execute("""
                    UPDATE person
                    SET name=?, surname=?, address=?, phone_number=?
                    WHERE identity_document=?
                """, person_data)
                connection.commit()
                return cursor.rowcount > 0
            except Error as e:
                print(f"Error: an error occurred while updating person data: {str(e)}")
                return False
    # End of update_person
    
    def delete_person(self, identity_document: str) -> bool:
        """Delete the person data into the database by identity document"""
        with self.db.get_connection() as connection:
            try:
                cursor = connection.cursor()
                cursor.execute("DELETE FROM person WHERE identity_document=?", (identity_document,))
                connection.commit()
                return cursor.rowcount > 0
            except Error as e:
                print(f"Error: an error occurred while deleting person data: {str(e)}")
                return False
    # End of delete_person