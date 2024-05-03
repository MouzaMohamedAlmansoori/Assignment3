import pickle  # Importing the pickle module for storing data in binay file format

# Define a class Venue
class Venue:  
    # Constructor method 
    def __init__(self, venue_id, name, address, contact, min_guests, max_guests):
        self.venue_id = venue_id  # Assigning venue ID
        self.name = name  # Assigning venue name
        self.address = address  # Assigning venue address
        self.contact = contact  # Assigning venue contact details
        self.min_guests = min_guests  # Assigning minimum number of guests for the venue
        self.max_guests = max_guests  # Assigning maximum number of guests for the venue

    @staticmethod
    # Method for adding a new venue to the data
    def add(venue_id, name, address, contact, min_guests, max_guests):
        # Creating a new venue object
        new_venue = Venue(venue_id, name, address, contact, min_guests, max_guests)
        # Opening file in append binary mode
        with open('venue_binary_data.pkl', 'ab') as file:
            # add venue data and writing to file
            pickle.dump(new_venue.__dict__, file)

    @staticmethod
    # Method for retrieving all venues from the data
    def retrieve_all_venues():
        all_venues = []  # Initialize an empty list for storing venues
        try:  # Try block for handling file operations
            # Opening file in read binary mode
            with open('venue_binary_data.pkl', 'rb') as file:
                while True:  # Loop for reading all venue data from the file
                    try:
                        # load venue data
                        venue_data = pickle.load(file)
                        # Append venue data to the list
                        all_venues.append(venue_data)
                    except EOFError:  # Handling end of file
                        break  # Exit loop when end of file is reached
        except FileNotFoundError:  # Handling file not found error
            pass  # Skip if file not found
        return all_venues  # Return the list of all venues

    @staticmethod
    # Method for deleting a venue from the data
    def delete_venue(venue_id):
        # Retrieve all venues
        venues = Venue.retrieve_all_venues()
        # Filter out venue to be deleted
        updated_venues = [venue for venue in venues if venue['venue_id'] != venue_id]
        # Opening file in write binary mode
        with open('venue_binary_data.pkl', 'wb') as file:
            for venue in updated_venues:  # Loop through updated venue list
                # write updated venue data to file
                pickle.dump(venue, file)

    @staticmethod
    # Method for modifying individual venue data
    def modify(venue_id, name, address, contact, min_guests, max_guests):
        # Retrieve all venues
        venues = Venue.retrieve_all_venues()
        for venue in venues:  # Loop through each venue
            if venue['venue_id'] == venue_id:  # Check if venue ID matches the specified ID
                # Update venue attributes
                venue['name'] = name
                venue['address'] = address
                venue['contact'] = contact
                venue['min_guests'] = min_guests
                venue['max_guests'] = max_guests
        # Opening file in write binary mode
        with open('venue_binary_data.pkl', 'wb') as file:
            for venue in venues:  # Loop through updated venue list
                # write updated venue data to file
                pickle.dump(venue, file)
