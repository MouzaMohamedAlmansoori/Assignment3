# Importing the pickle module for storing data in binay file format
import pickle  

# Define a class Client
class Client:  
    # Constructor method 
    def __init__(self, client_id, name, address, contact_details, budget):  
        self.client_id = client_id  # Assigning client ID
        self.name = name  # Assigning client name
        self.address = address  # Assigning client address
        self.contact_details = contact_details  # Assigning client contact details
        self.budget = budget  # Assigning client budget

    # Method for adding a new client to the data
    @staticmethod
    def add(client_id, name, address, contact_details, budget):  
        new_client = Client(client_id, name, address, contact_details, budget)  # Creating a new client object
        with open('client_binary_data.pkl', 'ab') as file:  # Opening file in append binary mode
            pickle.dump(new_client.__dict__, file)  # client data and writing to file

    # Method for retrieving all clients from the data
    @staticmethod
    def retrieve_all_clients():  
        all_clients = []  # Initialize an empty list for storing clients
        try:  # Try block for handling file operations
            with open('client_binary_data.pkl', 'rb') as file:  # Opening file in read binary mode
                while True:  # Loop for reading all client data from the file
                    try:
                        client_data = pickle.load(file)  # load client data
                        all_clients.append(client_data)  # Append client data to the list
                    except EOFError:  # Handling end of file
                        break  # Exit loop when end of file is reached
        except FileNotFoundError:  # Handling file not found error
            pass  # if file not found skip it
        return all_clients  # Return the list of all clients

    # Method for deleting a client from the data
    @staticmethod
    def delete_client(client_id):  
        clients = Client.retrieve_all_clients()  # Retrieve all clients
        updated_clients = [client for client in clients if client['client_id'] != client_id]  # Filter out client to be deleted
        with open('client_binary_data.pkl', 'wb') as file:  # Opening file in write binary mode
            for client in updated_clients:  # Loop through updated client list
                pickle.dump(client, file)  # write updated client data to file

    # Method for updating individual client data
    @staticmethod
    def retrieve_individual_client(client_id, new_name, new_address, new_contact_details, new_budget):  
        clients = Client.retrieve_all_clients()  # Retrieve all clients
        for client in clients:  # Loop through each client
            if client['client_id'] == client_id:  # Check if client ID matches the specified ID
                client['name'] = new_name  # Update client name
                client['address'] = new_address  # Update client address
                client['contact_details'] = new_contact_details  # Update client contact details
                client['budget'] = new_budget  # Update client budget
        with open('client_binary_data.pkl', 'wb') as file:  # Opening file in write binary mode
            for client in clients:  # Loop through updated client list
                pickle.dump(client, file)  # write updated client data to file

    # Method for retrieving individual client data for generating invoices
    @staticmethod
    def retrieve_individual_client_for_invoice(client_id):  
        try:  # Try block for handling file operations
            with open("client_binary_data.pkl", "rb") as file:  # Opening file in read binary mode
                try:  # Try block for reading client data from the file
                    while True:  # Loop for reading all client data from the file
                        client = pickle.load(file)  # load client data
                        if client['client_id'] == client_id:  # Check if client ID matches the specified ID
                            return client  # Return client data
                except EOFError:  # Handling end of file
                    pass  # End of file reached
        except FileNotFoundError:  # Handling file not found error
            print("Client data file not found.")  # Print error message if file not found
        return None  # Return None if client with specified ID not found
