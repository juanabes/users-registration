from model.person_model import PersonModel
from view.person_view import PersonView

class PersonController:
    """
    The controller handles user inputs from the View, interacts with the Model to perform bussiness logic (database operations), and updated the view
    """
    def __init__(self, model: PersonModel, view: PersonView):
        self.model = model
        self.view = view
        self.view.set_command_callbacks(
            create_command=self.handle_create_person,
            read_command=self.handle_read_person,
            update_command=self.handle_update_person,
            delete_command=self.handle_delete_person
        )
        
    def handle_create_person(self):
        """
        Handle the "Create" click event.
        1. Get inputs from the view
        2. Calls the Model to save the data
        3. Updates the View with the result.
        """
        
        person_data_dict = self.view.get_inputs()
        
        identity_document = person_data_dict["identity_document"]
        if not identity_document:
            self.view.display_message("Error: Identity Document is required", "orange")
            return
        
        person_data_tuple = (
            identity_document,
            person_data_dict["name"],
            person_data_dict["surname"],
            person_data_dict["address"],
            person_data_dict["phone_number"]
        )
        
        # Interact with model
        success = self.model.create_person(person_data_tuple)
        
        # Update view
        if success:
            self.view.display_message("Person created succesfully!", "#219ebc")
            self.view.clear_inputs_after_save()
        else:
            self.view.display_message("Error: couldn't create person (ID already exist)", "red")
    # End of handle_create_person
    
    def handle_read_person(self):
        """
        Handle the "Read" click event.
        1. Get Identity Document from view
        2. Model search Identity Document if doesn't exist return a message
        3. If Identity Document exist in database return all data 
        """
        person_data_dict = self.view.get_inputs()
        
        identity_document = person_data_dict["identity_document"]
        if not identity_document:
            self.view.display_message("Error: Identity Document is required to search person data", "orange")
            return 
        
        # Interact with model
        person_data = self.model.read_person(identity_document)
        
        # Update view
        if person_data:
            self.view.set_inputs(person_data[0], person_data[1], person_data[2], person_data[3], person_data[4])
            self.view.display_message("Person data loaded", "#8ecae6")
        else:
            self.view.display_message("Error: Person not found", "red")
    # End of handle_read_person
    
    def handle_update_person(self):
        """
        Handle the "Update" click event.
        1. Get Identity Document from the View
        2. Model search Identity Document, if doesn't exist return a message
        3. If Identity Document exists search all data affiliated with itself
        4. Get all data from entry fields to be updated
        5. Update the database
        """
        person_data_dict = self.view.get_inputs()
        
        identity_document = person_data_dict["identity_document"]
        if not identity_document:
            print("Check if ID exists or database is available")
            self.view.display_message("Error: Identity Document is required to update person data", "orange")
            return

        person_data_tuple = (
            person_data_dict["name"],
            person_data_dict["surname"],
            person_data_dict["address"],
            person_data_dict["phone_number"],
            identity_document
        )
        
        success = self.model.update_person(person_data_tuple)
        if success:
            self.view.display_message("Person data has been modify successfully!", "#8ecae6")
            self.view.clear_inputs_after_save()
        else:
            self.view.display_message("Person ID no exists", "red")
    # End of handle_update_person
    
    def handle_delete_person(self):
        """
        Handle the "Delete" click event.
        1. Get the Identity Document from the View
        2. Model search Identity Document, if doesn't exist return a message
        3. If Identity Document exists search all data affiliated with itself
        4. Delete all person data
        5. Update the database
        """
        person_data_dict = self.view.get_inputs()
        
        identity_document = person_data_dict["identity_document"]
        if not identity_document:
            self.view.display_message("Error: Identity Document is required to delete person data", "orange")
            return
        
        success = self.model.delete_person(identity_document)
        
        if success:
            self.view.display_message("Person has been deleted successfully!", "#8ecae6")
            self.view.clear_inputs_after_save()
        else:
            self.view.display_message("Person ID no exists", "red")
    # End of handle_delete_person
      
