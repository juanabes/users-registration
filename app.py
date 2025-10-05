import customtkinter as ctk

# Import all componentes
from model.database import Database
from model.person_model import PersonModel
from controller.person_controller import PersonController
from view.person_view import PersonView

def main():
    db = Database("database.db")
    db.create_tables()
    
    # Set the appearance and color theme for customtkinter
    ctk.set_appearance_mode("Dark")
    #ctk.set_default_color_theme("Default")
    
    # Create the window main
    window = ctk.CTk()
    
    # Instantiate Model and View
    model = PersonModel()
    view = PersonView(window)
    
    # Instantiate Controller, passing Model and View to link them
    # The Controller handles the wiring 
    controller = PersonController(model, view)
    
    # Start the application
    print("Application started")
    window.mainloop()
    print("Application closed")
    
    
if __name__ == "__main__":
    main()