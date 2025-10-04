import customtkinter as ctk

class PersonView:
    """
    A GUI class from person registrity using customtkinter.
    It provides a simple interface CRUD (Create, Read, Update, Delete) operations
    """
    def __init__(self, window):
        self.window = window
        
        # Configure the main window
        
        # Store commands callbacks (set by the controller)
        self.commands = {}

        # UI control variables linked to entry fields
        self.identity_document_var = ctk.StringVar(value="")
        self.name_var = ctk.StringVar(value="")
        self.surname_var = ctk.StringVar(value="")
        self.address_var = ctk.StringVar(value="")
        self.phone_number_var = ctk.StringVar(value="")
        self.message_var = ctk.StringVar(value="")
        
        # Label to display messages
        self.message_label = None
    
    def set_command_callbacks(self, create_command, read_command, update_command, delete_command):
        """
        Receives and stores the controller's handle methods
        """
        self.commands["create"] = create_command
        self.commands["read"] = read_command
        self.commands["update"] = update_command
        self.commands["delete"] = delete_command
    
    def get_inputs(self):
        """
        Get the values from entry fields, also create a dictionary and return it the values
        """
        return {
            "identity_document": self.identity_document_var.get().strip(),
            "name": self.name_var.get().strip(),
            "surname": self.surname_var.get().strip(),
            "address": self.address_var.get().strip(),
            "phone_number": self.phone_number_var.get().strip()
        }
        
    def display_message(self, message: str, color: str = "8ecae6"):
        """Update the message label with a message and a specific color"""
        pass
    
    def clear_inputs_after_save(self):
        """
        Clear all input fields and save the change come from model
        """
        self.identity_document_var.set("")
        self.name_var.set("")
        self.surname_var.set("")
        self.address_var.set("")
        self.phone_number_var.set("")