# Importing the pickle module for storing data in binay file format
import pickle  

class Event:
    # Constructor method 
    def __init__(self, event_id, event_type, theme, date, time, duration, venue_address, client_id, guest_list, 
                 catering_company, cleaning_company, decorations_company, entertainment_company, furniture_company, invoice):
        self.event_id = event_id  # Assigning event ID
        self.event_type = event_type  # Assigning event type
        self.theme = theme  # Assigning event theme
        self.date = date  # Assigning event date
        self.time = time  # Assigning event time
        self.duration = duration  # Assigning event duration
        self.venue_address = venue_address  # Assigning event venue address
        self.client_id = client_id  # Assigning client ID for the event
        self.guest_list = guest_list  # Assigning event guest list
        self.catering_company = catering_company  # Assigning catering company for the event
        self.cleaning_company = cleaning_company  # Assigning cleaning company for the event
        self.decorations_company = decorations_company  # Assigning decorations company for the event
        self.entertainment_company = entertainment_company  # Assigning entertainment company for the event
        self.furniture_company = furniture_company  # Assigning furniture company for the event
        self.invoice = invoice  # Assigning invoice for the event

    @staticmethod
    # Method for adding a new event to the data
    def add(event_id, event_type, theme, date, time, duration, venue_address, client_id, guest_list, 
            catering_company, cleaning_company, decorations_company, entertainment_company, furniture_company, invoice):
        # Creating a new event object
        new_event = Event(event_id, event_type, theme, date, time, duration, venue_address, client_id, guest_list, 
                          catering_company, cleaning_company, decorations_company, entertainment_company, furniture_company, invoice)
        # Opening file in append binary mode
        with open('event_binary_data.pkl', 'ab') as file:
            # update event data and writing to file
            pickle.dump(new_event.__dict__, file)

    @staticmethod
    # Method for retrieving all events from the data
    def retrieve_all_events():
        all_events = []  # Initialize an empty list for storing events
        try:  # Try block for handling file operations
            # Opening file in read binary mode
            with open('event_binary_data.pkl', 'rb') as file:
                while True:  # Loop for reading all event data from the file
                    try:
                        # load event data
                        event_data = pickle.load(file)  
                        # Append event data to the list
                        all_events.append(event_data)  
                    except EOFError:  # Handling end of file
                        break  # Exit loop when end of file is reached
        except FileNotFoundError:  # Handling file not found error
            pass  # Skip if file not found
        return all_events  # Return the list of all events

    @staticmethod
    # Method for deleting an event from the data
    def delete_event(event_id):  
        # Retrieve all events
        events = Event.retrieve_all_events()  
        # Filter out event to be deleted
        updated_events = [event for event in events if event['event_id'] != event_id]  
        # Opening file in write binary mode
        with open('event_binary_data.pkl', 'wb') as file:  
            for event in updated_events:  # Loop through updated event list
                # write updated event data to file
                pickle.dump(event, file)  

    @staticmethod
    # Method for modifying individual event data
    def modify(event_id, new_event_type, new_theme, new_date, new_time, new_duration, new_venue_address, new_client_id, new_guest_list, 
               new_catering_company, new_cleaning_company, new_decorations_company, new_entertainment_company, new_furniture_company, new_invoice):
        # Retrieve all events
        events = Event.retrieve_all_events()  
        for event in events:  # Loop through each event
            if event['event_id'] == event_id:  # Check if event ID matches the specified ID
                # Update event attributes
                event['event_type'] = new_event_type  
                event['theme'] = new_theme  
                event['date'] = new_date  
                event['time'] = new_time  
                event['duration'] = new_duration  
                event['venue_address'] = new_venue_address  
                event['client_id'] = new_client_id  
                event['guest_list'] = new_guest_list  
                event['catering_company'] = new_catering_company  
                event['cleaning_company'] = new_cleaning_company  
                event['decorations_company'] = new_decorations_company  
                event['entertainment_company'] = new_entertainment_company  
                event['furniture_company'] = new_furniture_company  
                event['invoice'] = new_invoice  
        # Opening file in write binary mode
        with open('event_binary_data.pkl', 'wb') as file:  
            for event in events:  # Loop through updated event list
                # write updated event data to file
                pickle.dump(event, file)  
