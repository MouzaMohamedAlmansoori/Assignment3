# Importing the pickle module for storing data in binay file format
import pickle  

class Supplier:
    # Constructor method 
    def __init__(self, supplier_id, name, address, contact_details, menu, min_num_of_guest, max_num_of_guest):
        self.supplier_id = supplier_id  # Assigning supplier ID
        self.name = name  # Assigning supplier name
        self.address = address  # Assigning supplier address
        self.contact_details = contact_details  # Assigning supplier contact details
        self.menu = menu  # Assigning supplier menu
        self.min_num_of_guest = min_num_of_guest  # Assigning minimum number of guests
        self.max_num_of_guest = max_num_of_guest  # Assigning maximum number of guests

    @classmethod
    # Method for adding a new supplier to the data
    def add(cls, supplier_id, name, address, contact_details, menu, min_num_of_guest, max_num_of_guest):
        # Creating a new supplier object
        new_supplier = cls(supplier_id, name, address, contact_details, menu, min_num_of_guest, max_num_of_guest)
        # Opening file in append binary mode
        with open('supplier_binary_data.pkl', 'ab') as file:
            # add supplier data and writing to file
            pickle.dump(new_supplier.__dict__, file)

    @classmethod
    # Method for retrieving all suppliers from the data
    def retrieve_all_suppliers(cls):
        all_suppliers = []  # Initialize an empty list for storing suppliers
        try:  # Try block for handling file operations
            # Opening file in read binary mode
            with open('supplier_binary_data.pkl', 'rb') as file:
                while True:  # Loop for reading all supplier data from the file
                    try:
                        # load supplier data
                        supplier_data = pickle.load(file)
                        # Append supplier data to the list
                        all_suppliers.append(supplier_data)
                    except EOFError:  # Handling end of file
                        break  # Exit loop when end of file is reached
        except FileNotFoundError:  # Handling file not found error
            pass  # Skip if file not found
        return all_suppliers  # Return the list of all suppliers

    @classmethod
    # Method for deleting a supplier from the data
    def delete_supplier(cls, supplier_id):
        # Retrieve all suppliers
        suppliers = cls.retrieve_all_suppliers()
        # Filter out supplier to be deleted
        updated_suppliers = [supplier for supplier in suppliers if supplier['supplier_id'] != supplier_id]
        # Opening file in write binary mode
        with open('supplier_binary_data.pkl', 'wb') as file:
            for supplier in updated_suppliers:  # Loop through updated supplier list
                # write updated supplier data to file
                pickle.dump(supplier, file)

    @classmethod
    # Method for modifying individual supplier data
    def modify(cls, supplier_id, new_name, new_address, new_contact_details, new_menu, new_min_num_of_guest, new_max_num_of_guest):
        # Retrieve all suppliers
        suppliers = cls.retrieve_all_suppliers()
        for supplier in suppliers:  # Loop through each supplier
            if supplier['supplier_id'] == supplier_id:  # Check if supplier ID matches the specified ID
                # Update supplier attributes
                supplier['name'] = new_name
                supplier['address'] = new_address
                supplier['contact_details'] = new_contact_details
                supplier['menu'] = new_menu
                supplier['min_num_of_guest'] = new_min_num_of_guest
                supplier['max_num_of_guest'] = new_max_num_of_guest
        # Opening file in write binary mode
        with open('supplier_binary_data.pkl', 'wb') as file:
            for supplier in suppliers:  # Loop through updated supplier list
                # write updated supplier data to file
                pickle.dump(supplier, file)
