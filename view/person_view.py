from tkinter import ttk
import customtkinter as ctk

class PersonView:
    BUTTON_RADIUS = 6
    BUTTON_WIDTH = 20
    
    """
    A GUI class from person registrity using customtkinter.
    It provides a simple interface CRUD (Create, Read, Update, Delete) operations
    """
    def __init__(self, window):
        self.window = window
        
        # Configure the main window
        self.window.title("Person registration")
        self.window.geometry("650x650")
        self.window.resizable(False, False)
        self.window.grid_rowconfigure(0, weight=0)
        self.window.grid_rowconfigure(1, weight=0)
        self.window.grid_rowconfigure(2, weight=1)
    
        self.window.grid_columnconfigure(0, weight=1)
        
        # Store commands callbacks (set by the controller)
        self.commands = {}
        
        # Common font for all labels
        self.label_font = ctk.CTkFont(size=16, family="Times New Roman", weight="bold")

        # UI control variables linked to entry fields
        self.identity_document_var = ctk.StringVar(value="")
        self.name_var = ctk.StringVar(value="")
        self.surname_var = ctk.StringVar(value="")
        self.address_var = ctk.StringVar(value="")
        self.phone_number_var = ctk.StringVar(value="")
        self.message_var = ctk.StringVar(value="")
        
        # Label to display messages
        self.message_label = None
        
        # Show app
        self.form_frame()
        self.crud_frame()
        self.table()
    
    def set_command_callbacks(self, create_command, read_command, update_command, delete_command):
        """
        Receives and stores the controller's handle methods
        """
        self.commands["create"] = create_command
        self.commands["read"] = read_command
        self.commands["update"] = update_command
        self.commands["delete"] = delete_command
    
    def display_message(self, message: str, color: str = "8ecae6"):
        """Update the message label with a message and a specific color"""
        # Update the text displayed via the variableS
        self.message_var.set(message)
        
        # Update the color of the message label
        self.message_label.configure(text_color=color)
        
        
    
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
    
    def set_inputs(self, identity_document, name, surname, address, phone_number):
        """Set the values of the input fields.
        Used by the Controller's read handler to display data
        """
        self.identity_document_var.set(identity_document)
        self.name_var.set(name)
        self.surname_var.set(surname)
        self.address_var.set(address)
        self.phone_number_var.set(phone_number)
    # End of set_inputs
    
    def clear_all_inputs(self):       
        """Clear all inputs fields and update message label"""
        empty = {}
        for key, value in self.get_inputs().items():
            if value == "":
                empty[key] = value
        if len(empty) == 5:
            return 
            
        self.identity_document_var.set("")
        self.name_var.set("")
        self.surname_var.set("")
        self.address_var.set("")
        self.phone_number_var.set("")
        self.display_message("All inputs are cleared", "#8ecae6") 
    # End of clear_all_inputs

    def clear_inputs_after_save(self):
        """
        Clear all input fields and save the change come from model
        """
        self.identity_document_var.set("")
        self.name_var.set("")
        self.surname_var.set("")
        self.address_var.set("")
        self.phone_number_var.set("")
    
    def create_person(self):
        """Calls the controller to create a new person"""
        if 'create' in self.commands:
            self.commands["create"]()
    # End of create person
    
    def read_person(self):
        """Calls the controller to read a person"""
        if 'read' in self.commands:        
            self.commands["read"]()
    # End of read_person
    
    def update_person(self):
        """Calls the controller to update person"""
        if 'update' in self.commands:
            self.commands["update"]()
    # End of update_person
        
    def delete_person(self):
        """Calls the controller to delete a person""" 
        if 'delete' in self.commands:
            self.commands["delete"]()
    
    def form_frame(self):
        """Creating the form frame"""
        form_frame = ctk.CTkFrame(
            self.window,
            fg_color="transparent"
        )
        form_frame.grid(row=0, column=0, pady=10, padx=10, sticky="nsew")

        # Configure from frame grids weights for better responsiveness
        for i in range(5):
            form_frame.grid_rowconfigure(i, weight=1)
        form_frame.grid_columnconfigure(0, weight=1)
        form_frame.grid_columnconfigure(1, weight=2)
        
        # Common justify
        justify="right"
        
        # Labels and their position
        labels = [
            ("Identity document:", 0, 0),
            ("Name:", 1, 0),
            ("Surname:", 2, 0),
            ("Address:", 3, 0),
            ("Phone number:", 4, 0)
        ]
        
        # Inputs fields and their linked variables
        inputs = [
            (self.identity_document_var, 0, 1),
            (self.name_var, 1, 1),
            (self.surname_var, 2, 1),
            (self.address_var, 3, 1),
            (self.phone_number_var, 4, 1)
        ]
        
        # Create labels fields in a loop
        for (name, row, column) in labels:
            lbl = ctk.CTkLabel(
                form_frame,
                text=name,
                font=self.label_font,
                justify=justify
            )
            lbl.grid(row=row, column=column, sticky="e")
        
        # Create inputs fields in a loop
        for (variable, row, column) in inputs:
            inp = ctk.CTkEntry(
                form_frame,
                textvariable=variable,
                fg_color="transparent"
            )
            inp.grid(row=row, column=column, pady=10, padx=(10, 20), sticky="ew")

        # Create label for messages
        self.message_label = ctk.CTkLabel(
            form_frame,
            textvariable=self.message_var,
            text_color="#8ecae6",
            font=self.label_font
        )
        self.message_label.grid(row=5, column=0, columnspan=2, pady=10, sticky="ew")

    def crud_frame(self):
        """Create frame with the CRUD buttons"""
        # Create the crud frame
        crud_frame = ctk.CTkFrame(
            self.window,
            fg_color="transparent"
        )
        
        # Grid in window's row 1
        crud_frame.grid(row=1, column=0, padx=20, pady=20, sticky="ew")
        
        # Configure frame grid weights for better responsiveness
        crud_frame.grid_rowconfigure(0, weight=1)
        for i in range(5):
            crud_frame.grid_columnconfigure(i, weight=1)
        
        # List of button configurations
        buttons = [
            ("Create", "#219ebc", self.create_person, 0, 0),
            ("Read", "#8ecae6", self.read_person, 0, 1),
            ("Update", "#ffb703", self.update_person, 0, 2),
            ("Delete", "#fb8500", self.delete_person, 0, 3),
            ("Clean", "#5c528f", self.clear_all_inputs, 0, 4)
        ]
        
        # Create buttons in a loop
        for (name, color, command, row, column) in buttons:
            btn = ctk.CTkButton(
                crud_frame,
                text=name,
                cursor="hand2",
                fg_color=color,
                text_color="black",
                corner_radius=self.BUTTON_RADIUS,
                width=self.BUTTON_WIDTH,
                command=command
            )
            btn.grid(row=row, column=column, padx=5, pady=3, sticky="nsew")
    
    def table(self):
        """Create and configure the Treeview table for displaying person data."""
        
        # Create a frame to hold the Treeview and Scrollbar
        table_frame = ctk.CTkFrame(self.window, fg_color="transparent")
        table_frame.grid(row=2, column=0, pady=(10, 20), padx=20, sticky="nsew")
        table_frame.grid_rowconfigure(0, weight=1)
        table_frame.grid_columnconfigure(0, weight=1)
        
        # Columns definition (Matching model/DB order)
        columns = ("#", "ID Document", "Name", "Surname", "Address", "Phone Number")
        
        self.data_table = ttk.Treeview(
            table_frame,
            columns=columns,
            show='headings',
            height=10
        )
        
        #  Configure Scrollbar 
        scrollbar = ctk.CTkScrollbar(table_frame, orientation="vertical", command=self.data_table.yview)
        self.data_table.configure(yscrollcommand=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky='ns')

        # --- Configure Columns ---
        
        # This is the implicit first column when using show='headings', often used for a row index
        self.data_table.column("#", width=30, anchor="center") 
        self.data_table.heading("#", text="No.")
        
        # ID Document (Primary key field, often wider)
        self.data_table.column("ID Document", width=100, anchor="w")
        self.data_table.heading("ID Document", text="ID Document")
        
        self.data_table.column("Name", width=100, anchor="w")
        self.data_table.heading("Name", text="Name")

        self.data_table.column("Surname", width=100, anchor="w")
        self.data_table.heading("Surname", text="Surname")

        self.data_table.column("Address", width=120, anchor="w")
        self.data_table.heading("Address", text="Address")

        self.data_table.column("Phone Number", width=100, anchor="w")
        self.data_table.heading("Phone Number", text="Phone Number")
        
        # Grid the table inside the frame
        self.data_table.grid(row=0, column=0, sticky="nsew")
        