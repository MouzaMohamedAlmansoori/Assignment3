# Importing the pickle module for storing data in binay file format
import pickle  

# Define a class Guest
class Guest:  
    # Constructor method 
    def __init__(self, guest_id, name, address, contact_details):
        self.guest_id = guest_id  # Assigning guest ID
        self.name = name  # Assigning guest name
        self.address = address  # Assigning guest address
        self.contact_details = contact_details  # Assigning guest contact details

    @staticmethod
    # Method for adding a new guest to the data
    def add(guest_id, name, address, contact_details):
        # Creating a new guest object
        new_guest = Guest(guest_id, name, address, contact_details)
        # Opening file in append binary mode
        with open('guest_binary_data.pkl', 'ab') as file:
            # add guest data and writing to file
            pickle.dump(new_guest.__dict__, file)

    @staticmethod
    # Method for retrieving all guests from the data
    def retrieve_all_guests():
        all_guests = []  # Initialize an empty list for storing guests
        try:  # Try block for handling file operations
            # Opening file in read binary mode
            with open('guest_binary_data.pkl', 'rb') as file:
                while True:  # Loop for reading all guest data from the file
                    try:
                        # load guest data
                        guest_data = pickle.load(file)
                        # Append guest data to the list
                        all_guests.append(guest_data)
                    except EOFError:  # Handling end of file
                        break  # Exit loop when end of file is reached
        except FileNotFoundError:  # Handling file not found error
            pass  # Skip if file not found
        return all_guests  # Return the list of all guests

    @staticmethod
    # Method for deleting a guest from the data
    def delete_guest(guest_id):
        # Retrieve all guests
        guests = Guest.retrieve_all_guests()
        # Filter out guest to be deleted
        updated_guests = [guest for guest in guests if guest['guest_id'] != guest_id]
        # Opening file in write binary mode
        with open('guest_binary_data.pkl', 'wb') as file:
            for guest in updated_guests:  # Loop through updated guest list
                # write updated guest data to file
                pickle.dump(guest, file)

    @staticmethod
    # Method for modifying individual guest data
    def modify(guest_id, new_name, new_address, new_contact_details):
        # Retrieve all guests
        guests = Guest.retrieve_all_guests()
        for guest in guests:  # Loop through each guest
            if guest['guest_id'] == guest_id:  # Check if guest ID matches the specified ID
                # Update guest attributes
                guest['name'] = new_name
                guest['address'] = new_address
                guest['contact_details'] = new_contact_details
        # Opening file in write binary mode
        with open('guest_binary_data.pkl', 'wb') as file:
            for guest in guests:  # Loop through updated guest list
                # write updated guest data to file
                pickle.dump(guest, file)
