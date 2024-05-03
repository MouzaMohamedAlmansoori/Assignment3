# Importing important libraries for GUI work
import tkinter as tk
from tkinter import messagebox
import tkcalendar

#Import classes from .py files
from client import Client
from employee import Employee
from event import Event
from guest import Guest
from venue import Venue
from supplier import Supplier

# Define EventManagementSystem class
class EventManagementSystem:
    # Styling dictionary for regular buttons
    button_style = {"bg": "#4d94ff", "fg": "black", "width": 20, "height": 2, "font": ("Arial", 12, "bold")}
    # Styling dictionary for submenu buttons
    button_style_submenu = {"bg": "#4d94ff", "fg": "black", "width": 30, "height": 2, "font": ("Arial", 12, "bold")}

# ************************************************************** Login Menu **************************************************************

    # Constructor method initializing the tkinter window
    def __init__(self):
        # Creating the tkinter window
        self.root = tk.Tk()
        self.root.title("Event Management System")  # Setting window title
        self.root.geometry("600x450")  # Setting window dimensions
        self.root.configure(background='#b3e0ff')  # Setting background color to light blue

        # Creating a menu bar
        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)

        # Creating a file menu
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Exit", command=self.root.quit)

        # Creating the main frame
        self.main_frame = tk.Frame(self.root, bg='#b3e0ff')  # Setting background color to light blue
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        self.selected_date = tk.StringVar()  # Variable for selected date

        self.state = "login"  # Initial state is login
        self.login_frame = None
        self.main_frame = None

        self.create_login_page()  # Creating the login page

    # Method to create the login page
    def create_login_page(self):
        self.clear_frames()  # Clearing any existing frames
        self.login_frame = tk.Frame(self.root, bg='#b3e0ff')  # Creating a frame for login page
        self.login_frame.pack(fill=tk.BOTH, expand=True)

        # Adding header label
        tk.Label(self.login_frame, text="Event Management System", bg='#b3e0ff', font=("Arial", 18, "bold")).pack(pady=20)

        # Username entry field
        tk.Label(self.login_frame, text="Username:", bg='#b3e0ff', font=("Arial", 12)).pack(pady=5)
        self.username_entry = tk.Entry(self.login_frame, font=("Arial", 12))
        self.username_entry.pack(pady=5, padx=20, ipady=4, ipadx=10)  # Adding padding and styling

        # Password entry field
        tk.Label(self.login_frame, text="Password:", bg='#b3e0ff', font=("Arial", 12)).pack(pady=5)
        self.password_entry = tk.Entry(self.login_frame, show="*", font=("Arial", 12))
        self.password_entry.pack(pady=5, padx=20, ipady=4, ipadx=10)  # Adding padding and styling

        # Login button
        login_btn = tk.Button(self.login_frame, text="Login", command=self.login, **self.button_style)
        login_btn.pack(pady=20)

    # Method for handling the login functionality
    def login(self):
        username = self.username_entry.get()  # Get the entered username
        password = self.password_entry.get()  # Get the entered password

        # Hardcoded username and password 
        if username == "student" and password == "123":
            self.state = "menu"  # Change state to menu
            self.show_menu()  # Show the menu
        else:
            messagebox.showerror("Error", "Invalid username or password")  # Show error message if login fails

# ************************************************************** Main Menu **************************************************************

    # Method to display the main menu options
    def show_menu(self):
        self.clear_frames()  # Clear any existing frames
        self.main_frame = tk.Frame(self.root, bg='#b3e0ff')  # Create a new frame for the main menu
        self.main_frame.pack(fill=tk.BOTH, expand=True)  

        # Creating buttons for each menu option with specified commands and styling
        client_btn = tk.Button(self.main_frame, text="Clients", command=self.open_client_menu, **self.button_style)
        client_btn.pack(pady=10) 

        employee_btn = tk.Button(self.main_frame, text="Employees", command=self.open_employee_menu, **self.button_style)
        employee_btn.pack(pady=10)  

        event_btn = tk.Button(self.main_frame, text="Events", command=self.open_event_menu, **self.button_style)
        event_btn.pack(pady=10)  

        guest_btn = tk.Button(self.main_frame, text="Guests", command=self.open_guest_menu, **self.button_style)
        guest_btn.pack(pady=10) 

        venue_btn = tk.Button(self.main_frame, text="Venues", command=self.open_venue_menu, **self.button_style)
        venue_btn.pack(pady=10) 

        supplier_btn = tk.Button(self.main_frame, text="Suppliers", command=self.open_supplier_menu, **self.button_style)
        supplier_btn.pack(pady=10)

    # Method to clear existing frames
    def clear_frames(self):
        if self.login_frame:  # Check if login frame exists
            self.login_frame.destroy()  # Destroy the login frame
        if self.main_frame:  # Check if main frame exists
            self.main_frame.destroy()  # Destroy the main frame


# ************************************************************** Client Section **************************************************************
    # Method to open the client management menu
    def open_client_menu(self):
        # Create a new window for client management
        client_window = tk.Toplevel(self.root)
        client_window.title("Client Management")
        client_window.geometry("400x380")
        client_window.configure(background='#b3e0ff')

        # Add buttons for different client management actions with specified commands and styling
        add_client_btn = tk.Button(client_window, text="Add Client Data", command=self.add_client_data, **self.button_style_submenu)
        add_client_btn.pack(pady=10)

        modify_client_btn = tk.Button(client_window, text="Modify Client Data", command=self.modify_client_data, **self.button_style_submenu)
        modify_client_btn.pack(pady=10)

        display_all_client_btn = tk.Button(client_window, text="Display All Client Data", command=self.display_all_client_data, **self.button_style_submenu)
        display_all_client_btn.pack(pady=10)

        delete_client_btn = tk.Button(client_window, text="Delete Client Data", command=self.delete_client_data, **self.button_style_submenu)
        delete_client_btn.pack(pady=10)

        invoice_btn = tk.Button(client_window, text="Show Invoice", command=lambda: self.take_client_id_input(), **self.button_style_submenu)
        invoice_btn.pack(pady=10)

    def add_client_data(self):
        # Create a new window for adding client data
        add_client_window = tk.Toplevel(self.root)
        add_client_window.title("Add Client Data")
        add_client_window.geometry("400x300")
        add_client_window.configure(background='#b3e0ff')

        # Frame for entries
        entry_frame = tk.Frame(add_client_window, bg='#b3e0ff')
        entry_frame.pack(pady=20)

        # Validation functions
        def validate_client_id():
            client_id = client_id_entry.get()
            if not client_id.isdigit():
                messagebox.showerror("Error", "Client ID must be a number")
                client_id_entry.delete(0, tk.END)

        # Validata name function
        def validate_name():
            name = name_entry.get()
            if not name.replace(" ", "").isalpha():
                messagebox.showerror("Error", "Name must contain only letters")
                name_entry.delete(0, tk.END)

        # validate address function
        def validate_address():
            address = address_entry.get()
            if len(address) == 0:
                messagebox.showerror("Error", "Address cannot be empty")

        # validate contact details
        def validate_contact_details():
            contact_details = contact_details_entry.get()
            if len(contact_details) == 0:
                messagebox.showerror("Error", "Contact details cannot be empty")

        # validate budget
        def validate_budget():
            budget = budget_entry.get()
            try:
                budget = float(budget)
                if budget <= 0:
                    messagebox.showerror("Error", "Budget must be a positive number")
            except ValueError:
                messagebox.showerror("Error", "Budget must be a number")

        # Labels and entry fields
        tk.Label(entry_frame, text="Client ID:", bg='#b3e0ff').grid(row=0, column=0, padx=10, pady=5, sticky="e")
        client_id_entry = tk.Entry(entry_frame)
        client_id_entry.grid(row=0, column=1, padx=10, pady=5)
        client_id_entry.bind("<FocusOut>", lambda e: validate_client_id())

        tk.Label(entry_frame, text="Name:", bg='#b3e0ff').grid(row=1, column=0, padx=10, pady=5, sticky="e")
        name_entry = tk.Entry(entry_frame)
        name_entry.grid(row=1, column=1, padx=10, pady=5)
        name_entry.bind("<FocusOut>", lambda e: validate_name())

        tk.Label(entry_frame, text="Address:", bg='#b3e0ff').grid(row=2, column=0, padx=10, pady=5, sticky="e")
        address_entry = tk.Entry(entry_frame)
        address_entry.grid(row=2, column=1, padx=10, pady=5)
        address_entry.bind("<FocusOut>", lambda e: validate_address())

        tk.Label(entry_frame, text="Contact Details:", bg='#b3e0ff').grid(row=3, column=0, padx=10, pady=5, sticky="e")
        contact_details_entry = tk.Entry(entry_frame)
        contact_details_entry.grid(row=3, column=1, padx=10, pady=5)
        contact_details_entry.bind("<FocusOut>", lambda e: validate_contact_details())

        tk.Label(entry_frame, text="Budget:", bg='#b3e0ff').grid(row=4, column=0, padx=10, pady=5, sticky="e")
        budget_entry = tk.Entry(entry_frame)
        budget_entry.grid(row=4, column=1, padx=10, pady=5)
        budget_entry.bind("<FocusOut>", lambda e: validate_budget())

        # Add client button
        add_client_button = tk.Button(add_client_window, text="Add Client", command=lambda: self.add_client_action(client_id_entry.get(), name_entry.get(), address_entry.get(), contact_details_entry.get(), budget_entry.get()), **self.button_style)
        add_client_button.pack(pady=10)

    def add_client_action(self, client_id, name, address, contact_details, budget):
        Client.add(client_id, name, address, contact_details, budget)
        messagebox.showinfo("Success", "Client added successfully!")


    # modify client data window
    def modify_client_data(self):
        modify_client_window = tk.Toplevel(self.root)
        modify_client_window.title("Modify Client Data")
        modify_client_window.geometry("400x300")
        modify_client_window.configure(background='#b3e0ff')

        # Label and entry field for client ID
        tk.Label(modify_client_window, text="Enter Client ID to modify:", bg='#b3e0ff').pack(pady=10)
        self.modify_client_id_entry = tk.Entry(modify_client_window)
        self.modify_client_id_entry.pack(pady=5)

        # Button to check client ID and open modify menu
        check_client_id_btn = tk.Button(modify_client_window, text="Check Client ID", command=self.check_client_id, **self.button_style)
        check_client_id_btn.pack(pady=10)

    # check client id function 
    def check_client_id(self):
        client_id = self.modify_client_id_entry.get()
        all_clients = Client.retrieve_all_clients()
        individual_client_data = None
        # loop to match client id
        for client_data in all_clients:
            if client_data['client_id'] == client_id:
                individual_client_data = client_data
                break
        if individual_client_data:
            self.show_modify_client_menu(individual_client_data)
        else:
            messagebox.showerror("Error", f"No client found with ID {client_id}.")

    # show modified client details
    def show_modify_client_menu(self, client_data):
        modify_client_window = tk.Toplevel(self.root)
        modify_client_window.title("Modify Client Data")
        modify_client_window.geometry("400x300")
        modify_client_window.configure(background='#b3e0ff')

        # Labels and entry fields for client data
        tk.Label(modify_client_window, text="Client ID:", bg='#b3e0ff').pack()
        tk.Label(modify_client_window, text=client_data['client_id'], bg='#b3e0ff').pack()

        tk.Label(modify_client_window, text="Name:", bg='#b3e0ff').pack()
        self.new_name_entry = tk.Entry(modify_client_window)
        self.new_name_entry.insert(tk.END, client_data['name'])
        self.new_name_entry.pack()

        tk.Label(modify_client_window, text="Address:", bg='#b3e0ff').pack()
        self.new_address_entry = tk.Entry(modify_client_window)
        self.new_address_entry.insert(tk.END, client_data['address'])
        self.new_address_entry.pack()

        tk.Label(modify_client_window, text="Contact Details:", bg='#b3e0ff').pack()
        self.new_contact_details_entry = tk.Entry(modify_client_window)
        self.new_contact_details_entry.insert(tk.END, client_data['contact_details'])
        self.new_contact_details_entry.pack()

        tk.Label(modify_client_window, text="Budget:", bg='#b3e0ff').pack()
        self.new_budget_entry = tk.Entry(modify_client_window)
        self.new_budget_entry.insert(tk.END, client_data['budget'])
        self.new_budget_entry.pack()

        # Button to submit modified client data
        submit_btn = tk.Button(modify_client_window, text="Submit", command=lambda: self.submit_modified_client_data(client_data['client_id']), **self.button_style)
        submit_btn.pack(pady=10)

    # submit modified details of client function
    def submit_modified_client_data(self, client_id):
        new_name = self.new_name_entry.get()
        new_address = self.new_address_entry.get()
        new_contact_details = self.new_contact_details_entry.get()
        new_budget = self.new_budget_entry.get()

        confirm = messagebox.askyesno("Confirm", f"Are you sure you want to modify client with ID {client_id}?")
        if confirm:
            Client.retrieve_individual_client(client_id, new_name, new_address, new_contact_details, new_budget)
            messagebox.showinfo("Success", f"Client with ID {client_id} modified successfully!")

    # display all client details
    def display_all_client_data(self):
        all_clients = Client.retrieve_all_clients()
        if all_clients:
            formatted_data = "\n".join([f"Client ID: {client['client_id']}\nName: {client['name']}\nAddress: {client['address']}\nContact Details: {client['contact_details']}\nBudget: {client['budget']}\n\n" for client in all_clients])
            self.display_data_window("All Clients", formatted_data)
        else:
            messagebox.showerror("Error", "No client data found.")

    # display data window creation function
    def display_data_window(self, title, data):
        data_window = tk.Toplevel(self.root)
        data_window.title(title)
        data_window.geometry("600x400")
        data_window.configure(background='#b3e0ff')

        text = tk.Text(data_window, bg='#b3e0ff')
        text.pack(fill=tk.BOTH, expand=True)

        text.insert(tk.END, data)

        scrollbar = tk.Scrollbar(data_window, command=text.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        text.config(yscrollcommand=scrollbar.set)

    # delete client data window create function 
    def delete_client_data(self):
        delete_client_window = tk.Toplevel(self.root)
        delete_client_window.title("Delete Client")
        delete_client_window.geometry("400x200")
        delete_client_window.configure(background='#b3e0ff')

        # Label and entry field for client ID
        tk.Label(delete_client_window, text="Enter Client ID to delete:", bg='#b3e0ff').pack(pady=10)
        self.delete_client_id_entry = tk.Entry(delete_client_window)
        self.delete_client_id_entry.pack(pady=5)

        # Button to delete client
        delete_client_btn = tk.Button(delete_client_window, text="Delete Client", command=self.delete_client_action, **self.button_style)
        delete_client_btn.pack(pady=10)

    # delete client action function 
    def delete_client_action(self):
        client_id = self.delete_client_id_entry.get()
        if client_id:
            confirm = messagebox.askyesno("Confirm", f"Are you sure you want to delete client with ID {client_id}?")
            if confirm:
                Client.delete_client(client_id)
                messagebox.showinfo("Success", f"Client with ID {client_id} deleted successfully!")
        else:
            messagebox.showerror("Error", "Please enter a valid client ID.")

    # client id input window create function
    def take_client_id_input(self):
        # Create a new window to take input for client ID
        client_id_window = tk.Toplevel(self.root)
        client_id_window.title("Enter Client ID")
        client_id_window.geometry("300x130")
        client_id_window.configure(background='#b3e0ff')

        # Label and entry field for client ID
        tk.Label(client_id_window, text="Enter Client ID:", bg='#b3e0ff').pack(pady=5)
        client_id_entry = tk.Entry(client_id_window)
        client_id_entry.pack(pady=5)

        # Button to confirm client ID input and show invoice
        confirm_btn = tk.Button(client_id_window, text="Show Invoice", command=lambda: self.show_invoice(client_id_entry.get()), **self.button_style)
        confirm_btn.pack(pady=5)

    # show invoice function
    def show_invoice(self, client_id):
        # Retrieve individual client data based on client ID
        client_data = Client.retrieve_individual_client_for_invoice(client_id)

        if client_data:
            # Format invoice details and payment pending information based on client data
            invoice_details = "Invoice Details for Client ID: " + client_id + "\n"
            invoice_details += "Name: " + client_data['name'] + "\n"
            invoice_details += "Address: " + client_data['address'] + "\n"
            invoice_details += "Contact Details: " + client_data['contact_details'] + "\n"
            invoice_details += "Budget: " + client_data['budget'] + "\n\n"

            payment_pending = "Payment Pending for Client ID: " + client_id + "\n"
            payment_pending += "Budget: " + client_data['budget'] + "\n"

            # Display invoice details and payment pending information in a new window
            invoice_window = tk.Toplevel(self.root)
            invoice_window.title("Invoice Details")
            invoice_window.geometry("400x400")
            invoice_window.configure(background='#b3e0ff')

            invoice_label = tk.Label(invoice_window, text=invoice_details, bg='#b3e0ff')
            invoice_label.pack(pady=10)

            pending_label = tk.Label(invoice_window, text=payment_pending, bg='#b3e0ff')
            pending_label.pack(pady=10)
        else:
            messagebox.showerror("Error", "Please enter a valid client ID.")

# ************************************************************** Employee Section **************************************************************

    # open employee menu create window
    def open_employee_menu(self):
        employee_window = tk.Toplevel(self.root)
        employee_window.title("Employee Management")
        employee_window.geometry("400x300")
        employee_window.configure(background='#b3e0ff')

        # add buttons and labels
        add_employee_btn = tk.Button(employee_window, text="Add Employee Data", command=self.add_employee_data, **self.button_style_submenu)
        add_employee_btn.pack(pady=10)

        modify_employee_btn = tk.Button(employee_window, text="Modify Employee Data", command=self.modify_employee_data, **self.button_style_submenu)
        modify_employee_btn.pack(pady=10)

        display_all_employee_btn = tk.Button(employee_window, text="Display All Employee Data", command=self.display_all_employee_data, **self.button_style_submenu)
        display_all_employee_btn.pack(pady=10)

        delete_employee_btn = tk.Button(employee_window, text="Delete Employee Data", command=self.delete_employee_data, **self.button_style_submenu)
        delete_employee_btn.pack(pady=10)

    # Add employee data function 
    def add_employee_data(self):
        add_employee_window = tk.Toplevel(self.root)
        add_employee_window.title("Add Employee Data")
        add_employee_window.geometry("400x400")
        add_employee_window.configure(background='#b3e0ff')

        # Frame for entries
        entry_frame = tk.Frame(add_employee_window, bg='#b3e0ff')
        entry_frame.pack(pady=20)

        # Labels and entry fields
        tk.Label(entry_frame, text="Name:", bg='#b3e0ff').grid(row=0, column=0, padx=10, pady=5, sticky="e")
        name_entry = tk.Entry(entry_frame)
        name_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(entry_frame, text="Employee ID:", bg='#b3e0ff').grid(row=1, column=0, padx=10, pady=5, sticky="e")
        emp_id_entry = tk.Entry(entry_frame)
        emp_id_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(entry_frame, text="Department:", bg='#b3e0ff').grid(row=2, column=0, padx=10, pady=5, sticky="e")
        department_entry = tk.Entry(entry_frame)
        department_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(entry_frame, text="Job Title:", bg='#b3e0ff').grid(row=3, column=0, padx=10, pady=5, sticky="e")
        job_title_entry = tk.Entry(entry_frame)
        job_title_entry.grid(row=3, column=1, padx=10, pady=5)

        tk.Label(entry_frame, text="Basic Salary:", bg='#b3e0ff').grid(row=4, column=0, padx=10, pady=5, sticky="e")
        basic_salary_entry = tk.Entry(entry_frame)
        basic_salary_entry.grid(row=4, column=1, padx=10, pady=5)

        tk.Label(entry_frame, text="Age:", bg='#b3e0ff').grid(row=5, column=0, padx=10, pady=5, sticky="e")
        age_entry = tk.Entry(entry_frame)
        age_entry.grid(row=5, column=1, padx=10, pady=5)

        tk.Label(entry_frame, text="Date of Birth:", bg='#b3e0ff').grid(row=6, column=0, padx=10, pady=5, sticky="e")
        dob_entry = tk.Entry(entry_frame)
        dob_entry.grid(row=6, column=1, padx=10, pady=5)

        tk.Label(entry_frame, text="Passport Details:", bg='#b3e0ff').grid(row=7, column=0, padx=10, pady=5, sticky="e")
        passport_details_entry = tk.Entry(entry_frame)
        passport_details_entry.grid(row=7, column=1, padx=10, pady=5)

        # Add employee button
        add_employee_button = tk.Button(add_employee_window, text="Add Employee", command=lambda: self.add_employee_action(name_entry.get(), emp_id_entry.get(), department_entry.get(), job_title_entry.get(), basic_salary_entry.get(), age_entry.get(), dob_entry.get(), passport_details_entry.get()), **self.button_style)
        add_employee_button.pack(pady=10)

    def add_employee_action(self, name, emp_id, department, job_title, basic_salary, age, dob, passport_details):
        Employee.add(name, emp_id, department, job_title, basic_salary, age, dob, passport_details)
        messagebox.showinfo("Success", "Employee added successfully!")

    # Create new window for delete employee
    def delete_employee_data(self):
        delete_employee_window = tk.Toplevel(self.root)
        delete_employee_window.title("Delete Employee")
        delete_employee_window.geometry("400x200")
        delete_employee_window.configure(background='#b3e0ff')

        # Label and entry field for employee ID
        tk.Label(delete_employee_window, text="Enter Employee ID to delete:", bg='#b3e0ff').pack(pady=10)
        self.delete_emp_id_entry = tk.Entry(delete_employee_window)
        self.delete_emp_id_entry.pack(pady=5)

        # Button to delete employee
        delete_employee_btn = tk.Button(delete_employee_window, text="Delete Employee", command=self.delete_employee_action, **self.button_style)
        delete_employee_btn.pack(pady=10)

    def delete_employee_action(self):
        emp_id = self.delete_emp_id_entry.get()
        if emp_id:
            confirm = messagebox.askyesno("Confirm", f"Are you sure you want to delete employee with ID {emp_id}?")
            if confirm:
                Employee.delete_employee(emp_id)
                messagebox.showinfo("Success", f"Employee with ID {emp_id} deleted successfully!")
        else:
            messagebox.showerror("Error", "Please enter a valid employee ID.")
    
    # Create modify employee data window
    def modify_employee_data(self):
        modify_employee_window = tk.Toplevel(self.root)
        modify_employee_window.title("Modify Employee Data")
        modify_employee_window.geometry("400x300")
        modify_employee_window.configure(background='#b3e0ff')

        # Label and entry field for employee ID
        tk.Label(modify_employee_window, text="Enter Employee ID to modify:", bg='#b3e0ff').pack(pady=10)
        self.modify_emp_id_entry = tk.Entry(modify_employee_window)
        self.modify_emp_id_entry.pack(pady=5)

        # Button to check employee ID and open modify menu
        check_emp_id_btn = tk.Button(modify_employee_window, text="Check Employee ID", command=self.check_emp_id, **self.button_style)
        check_emp_id_btn.pack(pady=10)

    def check_emp_id(self):
        emp_id = self.modify_emp_id_entry.get()
        all_employees = Employee.retrieve_all_employees()
        individual_employee_data = None
        for employee_data in all_employees:
            if employee_data['emp_id'] == emp_id:
                individual_employee_data = employee_data
                break
        if individual_employee_data:
            self.show_modify_employee_menu(individual_employee_data)
        else:
            messagebox.showerror("Error", f"No employee found with ID {emp_id}.")

    # Create Modify employee menu window
    def show_modify_employee_menu(self, employee_data):
        modify_employee_window = tk.Toplevel(self.root)
        modify_employee_window.title("Modify Employee Data")
        modify_employee_window.geometry("400x380")
        modify_employee_window.configure(background='#b3e0ff')

        # Labels and entry fields for employee data
        tk.Label(modify_employee_window, text="Employee ID:", bg='#b3e0ff').pack()
        tk.Label(modify_employee_window, text=employee_data['emp_id'], bg='#b3e0ff').pack()

        tk.Label(modify_employee_window, text="Name:", bg='#b3e0ff').pack()
        self.new_name_entry = tk.Entry(modify_employee_window)
        self.new_name_entry.insert(tk.END, employee_data['name'])
        self.new_name_entry.pack()

        tk.Label(modify_employee_window, text="Department:", bg='#b3e0ff').pack()
        self.new_department_entry = tk.Entry(modify_employee_window)
        self.new_department_entry.insert(tk.END, employee_data['department'])
        self.new_department_entry.pack()

        tk.Label(modify_employee_window, text="Job Title:", bg='#b3e0ff').pack()
        self.new_job_title_entry = tk.Entry(modify_employee_window)
        self.new_job_title_entry.insert(tk.END, employee_data['job_title'])
        self.new_job_title_entry.pack()

        tk.Label(modify_employee_window, text="Basic Salary:", bg='#b3e0ff').pack()
        self.new_basic_salary_entry = tk.Entry(modify_employee_window)
        self.new_basic_salary_entry.insert(tk.END, employee_data['basic_salary'])
        self.new_basic_salary_entry.pack()

        tk.Label(modify_employee_window, text="Age:", bg='#b3e0ff').pack()
        self.new_age_entry = tk.Entry(modify_employee_window)
        self.new_age_entry.insert(tk.END, employee_data['age'])
        self.new_age_entry.pack()

        tk.Label(modify_employee_window, text="Date of Birth:", bg='#b3e0ff').pack()
        self.new_dob_entry = tk.Entry(modify_employee_window)
        self.new_dob_entry.insert(tk.END, employee_data['dob'])
        self.new_dob_entry.pack()

        tk.Label(modify_employee_window, text="Passport Details:", bg='#b3e0ff').pack()
        self.new_passport_details_entry = tk.Entry(modify_employee_window)
        self.new_passport_details_entry.insert(tk.END, employee_data['passport_details'])
        self.new_passport_details_entry.pack()

        # Button to submit modified employee data
        submit_btn = tk.Button(modify_employee_window, text="Submit", command=lambda: self.submit_modified_employee_data(employee_data['emp_id']), **self.button_style)
        submit_btn.pack(pady=10)

    def submit_modified_employee_data(self, emp_id):
        new_name = self.new_name_entry.get()
        new_department = self.new_department_entry.get()
        new_job_title = self.new_job_title_entry.get()
        new_basic_salary = self.new_basic_salary_entry.get()
        new_age = self.new_age_entry.get()
        new_dob = self.new_dob_entry.get()
        new_passport_details = self.new_passport_details_entry.get()

        confirm = messagebox.askyesno("Confirm", f"Are you sure you want to modify employee with ID {emp_id}?")
        if confirm:
            # Call the modify_employee method from the Employee class
            Employee.modify(emp_id, new_name, new_department, new_job_title, new_basic_salary, new_age, new_dob, new_passport_details)
            messagebox.showinfo("Success", f"Employee with ID {emp_id} modified successfully!")

    # Display all employee data window
    def display_all_employee_data(self):
        all_employees = Employee.retrieve_all_employees()
        if all_employees:
            formatted_data = "\n".join([f"Employee ID: {employee['emp_id']}\nName: {employee['name']}\nDepartment: {employee['department']}\nJob Title: {employee['job_title']}\nBasic Salary: {employee['basic_salary']}\nAge: {employee['age']}\nDate of Birth: {employee['dob']}\nPassport Details: {employee['passport_details']}\n\n" for employee in all_employees])
            self.display_data_window("All Employees", formatted_data)
        else:
            messagebox.showerror("Error", "No employee data found.")

# ************************************************************** Event Section **************************************************************

    # Create event menu window
    def open_event_menu(self):
        event_window = tk.Toplevel(self.root)
        event_window.title("Event Management")
        event_window.geometry("400x350")  # Increased window size
        event_window.configure(background='#b3e0ff')

        # Add buttons and labels 
        add_event_btn = tk.Button(event_window, text="Add Event Data", command=self.add_event_data, **self.button_style_submenu)
        add_event_btn.pack(pady=10)

        modify_event_btn = tk.Button(event_window, text="Modify Event Data", command=self.modify_event_data, **self.button_style_submenu)
        modify_event_btn.pack(pady=10)

        display_all_event_btn = tk.Button(event_window, text="Display All Event Data", command=self.display_all_event_data, **self.button_style_submenu)
        display_all_event_btn.pack(pady=10)

        delete_event_btn = tk.Button(event_window, text="Delete Event Data", command=self.delete_event_data, **self.button_style_submenu)
        delete_event_btn.pack(pady=10)

    # Create add event data window   
    def add_event_data(self):
        add_event_window = tk.Toplevel(self.root)
        add_event_window.title("Add Event Data")
        add_event_window.geometry("400x580")
        add_event_window.configure(background='#b3e0ff')

        # Frame for entries
        entry_frame = tk.Frame(add_event_window, bg='#b3e0ff')
        entry_frame.pack(pady=20)

        # Labels and entry fields
        tk.Label(entry_frame, text="Event ID:", bg='#b3e0ff').grid(row=0, column=0, padx=10, pady=5, sticky="e")
        event_id_entry = tk.Entry(entry_frame)
        event_id_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(entry_frame, text="Event Type:", bg='#b3e0ff').grid(row=1, column=0, padx=10, pady=5, sticky="e")
        event_type_entry = tk.Entry(entry_frame)
        event_type_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(entry_frame, text="Theme:", bg='#b3e0ff').grid(row=2, column=0, padx=10, pady=5, sticky="e")
        theme_entry = tk.Entry(entry_frame)
        theme_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(entry_frame, text="Date:", bg='#b3e0ff').grid(row=3, column=0, padx=10, pady=5, sticky="e")
        # Button to open Calendar
        calendar_button = tk.Button(entry_frame, text="Open Calendar", command=self.open_calendar, bg='#b3e0ff', fg='black', font=('Arial', 12, 'bold'))
        calendar_button.grid(row=3, column=1, padx=10, pady=5)

        tk.Label(entry_frame, text="Time:", bg='#b3e0ff').grid(row=4, column=0, padx=10, pady=5, sticky="e")
        time_entry = tk.Entry(entry_frame)
        time_entry.grid(row=4, column=1, padx=10, pady=5)

        tk.Label(entry_frame, text="Duration:", bg='#b3e0ff').grid(row=5, column=0, padx=10, pady=5, sticky="e")
        duration_entry = tk.Entry(entry_frame)
        duration_entry.grid(row=5, column=1, padx=10, pady=5)

        tk.Label(entry_frame, text="Venue Address:", bg='#b3e0ff').grid(row=6, column=0, padx=10, pady=5, sticky="e")
        venue_address_entry = tk.Entry(entry_frame)
        venue_address_entry.grid(row=6, column=1, padx=10, pady=5)

        tk.Label(entry_frame, text="Client ID:", bg='#b3e0ff').grid(row=7, column=0, padx=10, pady=5, sticky="e")
        client_id_entry = tk.Entry(entry_frame)
        client_id_entry.grid(row=7, column=1, padx=10, pady=5)

        tk.Label(entry_frame, text="Guest List:", bg='#b3e0ff').grid(row=8, column=0, padx=10, pady=5, sticky="e")
        guest_list_entry = tk.Entry(entry_frame)
        guest_list_entry.grid(row=8, column=1, padx=10, pady=5)

        tk.Label(entry_frame, text="Catering Company:", bg='#b3e0ff').grid(row=9, column=0, padx=10, pady=5, sticky="e")
        catering_company_entry = tk.Entry(entry_frame)
        catering_company_entry.grid(row=9, column=1, padx=10, pady=5)

        tk.Label(entry_frame, text="Cleaning Company:", bg='#b3e0ff').grid(row=10, column=0, padx=10, pady=5, sticky="e")
        cleaning_company_entry = tk.Entry(entry_frame)
        cleaning_company_entry.grid(row=10, column=1, padx=10, pady=5)

        tk.Label(entry_frame, text="Decorations Company:", bg='#b3e0ff').grid(row=11, column=0, padx=10, pady=5, sticky="e")
        decorations_company_entry = tk.Entry(entry_frame)
        decorations_company_entry.grid(row=11, column=1, padx=10, pady=5)

        tk.Label(entry_frame, text="Entertainment Company:", bg='#b3e0ff').grid(row=12, column=0, padx=10, pady=5, sticky="e")
        entertainment_company_entry = tk.Entry(entry_frame)
        entertainment_company_entry.grid(row=12, column=1, padx=10, pady=5)

        tk.Label(entry_frame, text="Furniture Company:", bg='#b3e0ff').grid(row=13, column=0, padx=10, pady=5, sticky="e")
        furniture_company_entry = tk.Entry(entry_frame)
        furniture_company_entry.grid(row=13, column=1, padx=10, pady=5)

        tk.Label(entry_frame, text="Invoice:", bg='#b3e0ff').grid(row=14, column=0, padx=10, pady=5, sticky="e")
        invoice_entry = tk.Entry(entry_frame)
        invoice_entry.grid(row=14, column=1, padx=10, pady=5)

        # Add event button
        add_event_button = tk.Button(add_event_window, text="Add Event", command=lambda: self.add_event_action(event_id_entry.get(), event_type_entry.get(), theme_entry.get(), self.selected_date.get(), time_entry.get(), duration_entry.get(), venue_address_entry.get(), client_id_entry.get(), guest_list_entry.get(), catering_company_entry.get(), cleaning_company_entry.get(), decorations_company_entry.get(), entertainment_company_entry.get(), furniture_company_entry.get(), invoice_entry.get()), **self.button_style)
        add_event_button.pack(pady=10)

    # Create open calendar window
    def open_calendar(self):
        calendar_window = tk.Toplevel(self.root)
        calendar_window.title("Select Date")
        calendar_window.geometry("300x280")
        calendar_window.configure(background='#b3e0ff')
        
        # Calendar widget
        calendar = tkcalendar.Calendar(calendar_window, selectmode="day")
        calendar.pack(pady=20)

        # Function to retrieve selected date
        def get_selected_date():
            self.selected_date.set(calendar.get_date())
            calendar_window.destroy()

        # Button to confirm date selection
        confirm_button = tk.Button(calendar_window, text="Confirm", command=get_selected_date)
        confirm_button.pack(pady=10)

    def add_event_action(self, event_id, event_type, theme, date, time, duration, venue_address, client_id, guest_list, catering_company, cleaning_company, decorations_company, entertainment_company, furniture_company, invoice):
        Event.add(event_id, event_type, theme, date, time, duration, venue_address, client_id, guest_list, catering_company, cleaning_company, decorations_company, entertainment_company, furniture_company, invoice)
        messagebox.showinfo("Success", "Event added successfully!")

    # Create delete event window
    def delete_event_data(self):
        delete_event_window = tk.Toplevel(self.root)
        delete_event_window.title("Delete Event")
        delete_event_window.geometry("400x200")
        delete_event_window.configure(background='#b3e0ff')

        # Label and entry field for event ID
        tk.Label(delete_event_window, text="Enter Event ID to delete:", bg='#b3e0ff').pack(pady=10)
        self.delete_event_id_entry = tk.Entry(delete_event_window)
        self.delete_event_id_entry.pack(pady=5)

        # Button to delete event
        delete_event_btn = tk.Button(delete_event_window, text="Delete Event", command=self.delete_event_action, **self.button_style)
        delete_event_btn.pack(pady=10)

    def delete_event_action(self):
        event_id = self.delete_event_id_entry.get()
        if event_id:
            confirm = messagebox.askyesno("Confirm", f"Are you sure you want to delete event with ID {event_id}?")
            if confirm:
                Event.delete_event(event_id)
                messagebox.showinfo("Success", f"Event with ID {event_id} deleted successfully!")
        else:
            messagebox.showerror("Error", "Please enter a valid event ID.")

    # Create modify event window
    def modify_event_data(self):
        modify_event_window = tk.Toplevel(self.root)
        modify_event_window.title("Modify Event Data")
        modify_event_window.geometry("400x300")
        modify_event_window.configure(background='#b3e0ff')

        # Label and entry field for event ID
        tk.Label(modify_event_window, text="Enter Event ID to modify:", bg='#b3e0ff').pack(pady=10)
        self.modify_event_id_entry = tk.Entry(modify_event_window)
        self.modify_event_id_entry.pack(pady=5)

        # Button to check event ID and open modify menu
        check_event_id_btn = tk.Button(modify_event_window, text="Check Event ID", command=self.check_event_id, **self.button_style)
        check_event_id_btn.pack(pady=10)

    def check_event_id(self):
        event_id = self.modify_event_id_entry.get()
        all_events = Event.retrieve_all_events()
        individual_event_data = None
        for event_data in all_events:
            if event_data['event_id'] == event_id:
                individual_event_data = event_data
                break
        if individual_event_data:
            self.show_modify_event_menu(individual_event_data)
        else:
            messagebox.showerror("Error", f"No event found with ID {event_id}.")

    # Create modify event window
    def show_modify_event_menu(self, event_data):
        modify_event_window = tk.Toplevel(self.root)
        modify_event_window.title("Modify Event Data")
        modify_event_window.geometry("400x650")
        modify_event_window.configure(background='#b3e0ff')

        # Labels and entry fields for event data
        tk.Label(modify_event_window, text="Event ID:", bg='#b3e0ff').pack()
        tk.Label(modify_event_window, text=event_data['event_id'], bg='#b3e0ff').pack()

        tk.Label(modify_event_window, text="Event Type:", bg='#b3e0ff').pack()
        self.new_event_type_entry = tk.Entry(modify_event_window)
        self.new_event_type_entry.insert(tk.END, event_data['event_type'])
        self.new_event_type_entry.pack()

        tk.Label(modify_event_window, text="Theme:", bg='#b3e0ff').pack()
        self.new_theme_entry = tk.Entry(modify_event_window)
        self.new_theme_entry.insert(tk.END, event_data['theme'])
        self.new_theme_entry.pack()

        tk.Label(modify_event_window, text="Date:", bg='#b3e0ff').pack()
        self.new_date_entry = tk.Entry(modify_event_window)
        self.new_date_entry.insert(tk.END, event_data['date'])
        self.new_date_entry.pack()

        tk.Label(modify_event_window, text="Time:", bg='#b3e0ff').pack()
        self.new_time_entry = tk.Entry(modify_event_window)
        self.new_time_entry.insert(tk.END, event_data['time'])
        self.new_time_entry.pack()

        tk.Label(modify_event_window, text="Duration:", bg='#b3e0ff').pack()
        self.new_duration_entry = tk.Entry(modify_event_window)
        self.new_duration_entry.insert(tk.END, event_data['duration'])
        self.new_duration_entry.pack()

        tk.Label(modify_event_window, text="Venue Address:", bg='#b3e0ff').pack()
        self.new_venue_address_entry = tk.Entry(modify_event_window)
        self.new_venue_address_entry.insert(tk.END, event_data['venue_address'])
        self.new_venue_address_entry.pack()

        tk.Label(modify_event_window, text="Client ID:", bg='#b3e0ff').pack()
        self.new_client_id_entry = tk.Entry(modify_event_window)
        self.new_client_id_entry.insert(tk.END, event_data['client_id'])
        self.new_client_id_entry.pack()

        tk.Label(modify_event_window, text="Guest List:", bg='#b3e0ff').pack()
        self.new_guest_list_entry = tk.Entry(modify_event_window)
        self.new_guest_list_entry.insert(tk.END, event_data['guest_list'])
        self.new_guest_list_entry.pack()

        tk.Label(modify_event_window, text="Catering Company:", bg='#b3e0ff').pack()
        self.new_catering_company_entry = tk.Entry(modify_event_window)
        self.new_catering_company_entry.insert(tk.END, event_data['catering_company'])
        self.new_catering_company_entry.pack()

        tk.Label(modify_event_window, text="Cleaning Company:", bg='#b3e0ff').pack()
        self.new_cleaning_company_entry = tk.Entry(modify_event_window)
        self.new_cleaning_company_entry.insert(tk.END, event_data['cleaning_company'])
        self.new_cleaning_company_entry.pack()

        tk.Label(modify_event_window, text="Decorations Company:", bg='#b3e0ff').pack()
        self.new_decorations_company_entry = tk.Entry(modify_event_window)
        self.new_decorations_company_entry.insert(tk.END, event_data['decorations_company'])
        self.new_decorations_company_entry.pack()

        tk.Label(modify_event_window, text="Entertainment Company:", bg='#b3e0ff').pack()
        self.new_entertainment_company_entry = tk.Entry(modify_event_window)
        self.new_entertainment_company_entry.insert(tk.END, event_data['entertainment_company'])
        self.new_entertainment_company_entry.pack()

        tk.Label(modify_event_window, text="Furniture Company:", bg='#b3e0ff').pack()
        self.new_furniture_company_entry = tk.Entry(modify_event_window)
        self.new_furniture_company_entry.insert(tk.END, event_data['furniture_company'])
        self.new_furniture_company_entry.pack()

        tk.Label(modify_event_window, text="Invoice:", bg='#b3e0ff').pack()
        self.new_invoice_entry = tk.Entry(modify_event_window)
        self.new_invoice_entry.insert(tk.END, event_data['invoice'])
        self.new_invoice_entry.pack()

        # Button to submit modified event data
        submit_btn = tk.Button(modify_event_window, text="Submit", command=lambda: self.submit_modified_event_data(event_data['event_id']), **self.button_style)
        submit_btn.pack(pady=10)

    def submit_modified_event_data(self, event_id):
        new_event_type = self.new_event_type_entry.get()
        new_theme = self.new_theme_entry.get()
        new_date = self.new_date_entry.get()
        new_time = self.new_time_entry.get()
        new_duration = self.new_duration_entry.get()
        new_venue_address = self.new_venue_address_entry.get()
        new_client_id = self.new_client_id_entry.get()
        new_guest_list = self.new_guest_list_entry.get()
        new_catering_company = self.new_catering_company_entry.get()
        new_cleaning_company = self.new_cleaning_company_entry.get()
        new_decorations_company = self.new_decorations_company_entry.get()
        new_entertainment_company = self.new_entertainment_company_entry.get()
        new_furniture_company = self.new_furniture_company_entry.get()
        new_invoice = self.new_invoice_entry.get()

        confirm = messagebox.askyesno("Confirm", f"Are you sure you want to modify event with ID {event_id}?")
        if confirm:
            # Call the modify_event method from the Event class
            Event.modify(event_id, new_event_type, new_theme, new_date, new_time, new_duration, new_venue_address, new_client_id, new_guest_list, new_catering_company, new_cleaning_company, new_decorations_company, new_entertainment_company, new_furniture_company, new_invoice)
            messagebox.showinfo("Success", f"Event with ID {event_id} modified successfully!")

    # Display all events data
    def display_all_event_data(self):
        all_events = Event.retrieve_all_events()
        if all_events:
            formatted_data = "\n".join([f"Event ID: {event['event_id']}\nEvent Type: {event['event_type']}\nTheme: {event['theme']}\nDate: {event['date']}\nTime: {event['time']}\nDuration: {event['duration']}\nVenue Address: {event['venue_address']}\nClient ID: {event['client_id']}\nGuest List: {event['guest_list']}\nCatering Company: {event['catering_company']}\nCleaning Company: {event['cleaning_company']}\nDecorations Company: {event['decorations_company']}\nEntertainment Company: {event['entertainment_company']}\nFurniture Company: {event['furniture_company']}\nInvoice: {event['invoice']}\n\n" for event in all_events])
            self.display_data_window("All Events", formatted_data)
        else:
            messagebox.showerror("Error", "No event data found.")

# ************************************************************** Guest Section **************************************************************

    # Create Guest menu window
    def open_guest_menu(self):
        guest_window = tk.Toplevel(self.root)
        guest_window.title("Guest Management")
        guest_window.geometry("400x300")
        guest_window.configure(background='#b3e0ff')

        # Add buttons and laels
        add_guest_btn = tk.Button(guest_window, text="Add Guest Data", command=self.add_guest_data, **self.button_style_submenu)
        add_guest_btn.pack(pady=10)

        modify_guest_btn = tk.Button(guest_window, text="Modify Guest Data", command=self.modify_guest_data, **self.button_style_submenu)
        modify_guest_btn.pack(pady=10)

        display_all_guest_btn = tk.Button(guest_window, text="Display All Guest Data", command=self.display_all_guest_data, **self.button_style_submenu)
        display_all_guest_btn.pack(pady=10)

        delete_guest_btn = tk.Button(guest_window, text="Delete Guest Data", command=self.delete_guest_data, **self.button_style_submenu)
        delete_guest_btn.pack(pady=10)

    # Create a new window for adding guest data
    def add_guest_data(self):
        add_guest_window = tk.Toplevel(self.root)
        add_guest_window.title("Add Guest Data")
        add_guest_window.geometry("400x300")
        add_guest_window.configure(background='#b3e0ff')

        # Frame for entries
        entry_frame = tk.Frame(add_guest_window, bg='#b3e0ff')
        entry_frame.pack(pady=20)

        # Labels and entry fields
        tk.Label(entry_frame, text="Name:", bg='#b3e0ff').grid(row=0, column=0, padx=10, pady=5, sticky="e")
        name_entry = tk.Entry(entry_frame)
        name_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(entry_frame, text="Guest ID:", bg='#b3e0ff').grid(row=1, column=0, padx=10, pady=5, sticky="e")
        guest_id_entry = tk.Entry(entry_frame)
        guest_id_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(entry_frame, text="Address:", bg='#b3e0ff').grid(row=2, column=0, padx=10, pady=5, sticky="e")
        address_entry = tk.Entry(entry_frame)
        address_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(entry_frame, text="Contact Details:", bg='#b3e0ff').grid(row=3, column=0, padx=10, pady=5, sticky="e")
        contact_entry = tk.Entry(entry_frame)
        contact_entry.grid(row=3, column=1, padx=10, pady=5)

        # Add guest button
        add_guest_button = tk.Button(add_guest_window, text="Add Guest", command=lambda: self.add_guest_action(name_entry.get(), guest_id_entry.get(), address_entry.get(), contact_entry.get()), **self.button_style)
        add_guest_button.pack(pady=10)

    def add_guest_action(self, name, guest_id, address, contact_details):
        Guest.add(guest_id, name, address, contact_details)
        messagebox.showinfo("Success", "Guest added successfully!")

    # Create a new window for deleting guest data
    def delete_guest_data(self):
        delete_guest_window = tk.Toplevel(self.root)
        delete_guest_window.title("Delete Guest")
        delete_guest_window.geometry("400x200")
        delete_guest_window.configure(background='#b3e0ff')

        # Label and entry field for guest ID
        tk.Label(delete_guest_window, text="Enter Guest ID to delete:", bg='#b3e0ff').pack(pady=10)
        self.delete_guest_id_entry = tk.Entry(delete_guest_window)
        self.delete_guest_id_entry.pack(pady=5)

        # Button to delete guest
        delete_guest_btn = tk.Button(delete_guest_window, text="Delete Guest", command=self.delete_guest_action, **self.button_style)
        delete_guest_btn.pack(pady=10)

    def delete_guest_action(self):
        guest_id = self.delete_guest_id_entry.get()
        all_guests = Guest.retrieve_all_guests()
        if guest_id:
            if any(guest['guest_id'] == guest_id for guest in all_guests):
                confirm = messagebox.askyesno("Confirm", f"Are you sure you want to delete guest with ID {guest_id}?")
                if confirm:
                    Guest.delete_guest(guest_id)
                    messagebox.showinfo("Success", f"Guest with ID {guest_id} deleted successfully!")
            else:
                messagebox.showerror("Error", f"No guest found with ID {guest_id}.")
        else:
            messagebox.showerror("Error", "Please enter a valid guest ID.")

    # Create a new window for modify guest data
    def modify_guest_data(self):
        modify_guest_window = tk.Toplevel(self.root)
        modify_guest_window.title("Modify Guest Data")
        modify_guest_window.geometry("400x300")
        modify_guest_window.configure(background='#b3e0ff')

        # Label and entry field for guest ID
        tk.Label(modify_guest_window, text="Enter Guest ID to modify:", bg='#b3e0ff').pack(pady=10)
        self.modify_guest_id_entry = tk.Entry(modify_guest_window)
        self.modify_guest_id_entry.pack(pady=5)

        # Button to check guest ID and open modify menu
        check_guest_id_btn = tk.Button(modify_guest_window, text="Check Guest ID", command=self.check_guest_id, **self.button_style)
        check_guest_id_btn.pack(pady=10)

    def check_guest_id(self):
        guest_id = self.modify_guest_id_entry.get()
        all_guests = Guest.retrieve_all_guests()
        individual_guest_data = None
        for guest_data in all_guests:
            if guest_data['guest_id'] == guest_id:
                individual_guest_data = guest_data
                break
        if individual_guest_data:
            self.show_modify_guest_menu(individual_guest_data)
        else:
            messagebox.showerror("Error", f"No guest found with ID {guest_id}.")

    # Create a new window for modify guest data
    def show_modify_guest_menu(self, guest_data):
        modify_guest_window = tk.Toplevel(self.root)
        modify_guest_window.title("Modify Guest Data")
        modify_guest_window.geometry("400x260")
        modify_guest_window.configure(background='#b3e0ff')

        # Labels and entry fields for guest data
        tk.Label(modify_guest_window, text="Guest ID:", bg='#b3e0ff').pack()
        tk.Label(modify_guest_window, text=guest_data['guest_id'], bg='#b3e0ff').pack()

        tk.Label(modify_guest_window, text="Name:", bg='#b3e0ff').pack()
        self.new_name_entry = tk.Entry(modify_guest_window)
        self.new_name_entry.insert(tk.END, guest_data['name'])
        self.new_name_entry.pack()

        tk.Label(modify_guest_window, text="Address:", bg='#b3e0ff').pack()
        self.new_address_entry = tk.Entry(modify_guest_window)
        self.new_address_entry.insert(tk.END, guest_data['address'])
        self.new_address_entry.pack()

        tk.Label(modify_guest_window, text="Contact Details:", bg='#b3e0ff').pack()
        self.new_contact_entry = tk.Entry(modify_guest_window)
        self.new_contact_entry.insert(tk.END, guest_data['contact_details'])
        self.new_contact_entry.pack()

        # Button to submit modified guest data
        submit_btn = tk.Button(modify_guest_window, text="Submit", command=lambda: self.submit_modified_guest_data(guest_data['guest_id']), **self.button_style)
        submit_btn.pack(pady=10)

    def submit_modified_guest_data(self, guest_id):
        new_name = self.new_name_entry.get()
        new_address = self.new_address_entry.get()
        new_contact_details = self.new_contact_entry.get()

        confirm = messagebox.askyesno("Confirm", f"Are you sure you want to modify guest with ID {guest_id}?")
        if confirm:
            Guest.modify(guest_id, new_name, new_address, new_contact_details)
            messagebox.showinfo("Success", f"Guest with ID {guest_id} modified successfully!")

    # Create a new window for display all guest data
    def display_all_guest_data(self):
        all_guests = Guest.retrieve_all_guests()
        if all_guests:
            formatted_data = "\n".join([f"Guest ID: {guest['guest_id']}\nName: {guest['name']}\nAddress: {guest['address']}\nContact Details: {guest['contact_details']}\n\n" for guest in all_guests])
            self.display_data_window("All Guests", formatted_data)
        else:
            messagebox.showerror("Error", "No guest data found.")

# ************************************************************** Venue Section **************************************************************
    # Create a new window for Venue menu
    def open_venue_menu(self):
        venue_window = tk.Toplevel(self.root)
        venue_window.title("Venue Management")
        venue_window.geometry("400x300")
        venue_window.configure(background='#b3e0ff')

        # Add buttons and labels
        add_venue_btn = tk.Button(venue_window, text="Add Venue Data", command=self.add_venue_data, **self.button_style_submenu)
        add_venue_btn.pack(pady=10)

        modify_venue_btn = tk.Button(venue_window, text="Modify Venue Data", command=self.modify_venue_data, **self.button_style_submenu)
        modify_venue_btn.pack(pady=10)

        display_all_venue_btn = tk.Button(venue_window, text="Display All Venue Data", command=self.display_all_venue_data, **self.button_style_submenu)
        display_all_venue_btn.pack(pady=10)

        delete_venue_btn = tk.Button(venue_window, text="Delete Venue Data", command=self.delete_venue_data, **self.button_style_submenu)
        delete_venue_btn.pack(pady=10)

    # Create a new window for adding venue data
    def add_venue_data(self):
        add_venue_window = tk.Toplevel(self.root)
        add_venue_window.title("Add Venue Data")
        add_venue_window.geometry("400x400")
        add_venue_window.configure(background='#b3e0ff')

        # Frame for entries
        entry_frame = tk.Frame(add_venue_window, bg='#b3e0ff')
        entry_frame.pack(pady=20)

        # Labels and entry fields
        tk.Label(entry_frame, text="Name:", bg='#b3e0ff').grid(row=0, column=0, padx=10, pady=5, sticky="e")
        name_entry = tk.Entry(entry_frame)
        name_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(entry_frame, text="Venue ID:", bg='#b3e0ff').grid(row=1, column=0, padx=10, pady=5, sticky="e")
        venue_id_entry = tk.Entry(entry_frame)
        venue_id_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(entry_frame, text="Address:", bg='#b3e0ff').grid(row=2, column=0, padx=10, pady=5, sticky="e")
        address_entry = tk.Entry(entry_frame)
        address_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(entry_frame, text="Contact:", bg='#b3e0ff').grid(row=3, column=0, padx=10, pady=5, sticky="e")
        contact_entry = tk.Entry(entry_frame)
        contact_entry.grid(row=3, column=1, padx=10, pady=5)

        tk.Label(entry_frame, text="Min Guests:", bg='#b3e0ff').grid(row=4, column=0, padx=10, pady=5, sticky="e")
        min_guests_entry = tk.Entry(entry_frame)
        min_guests_entry.grid(row=4, column=1, padx=10, pady=5)

        tk.Label(entry_frame, text="Max Guests:", bg='#b3e0ff').grid(row=5, column=0, padx=10, pady=5, sticky="e")
        max_guests_entry = tk.Entry(entry_frame)
        max_guests_entry.grid(row=5, column=1, padx=10, pady=5)

        # Add venue button
        add_venue_button = tk.Button(add_venue_window, text="Add Venue", command=lambda: self.add_venue_action(venue_id_entry.get(), name_entry.get(), address_entry.get(), contact_entry.get(), min_guests_entry.get(), max_guests_entry.get()), **self.button_style)
        add_venue_button.pack(pady=10)

    def add_venue_action(self, name, venue_id, address, contact, min_guests, max_guests):
        Venue.add(name, venue_id, address, contact, min_guests, max_guests)
        messagebox.showinfo("Success", "Venue added successfully!")

    # Create a new window for delete venue data
    def delete_venue_data(self):
        delete_venue_window = tk.Toplevel(self.root)
        delete_venue_window.title("Delete Venue")
        delete_venue_window.geometry("400x200")
        delete_venue_window.configure(background='#b3e0ff')

        # Label and entry field for venue ID
        tk.Label(delete_venue_window, text="Enter Venue ID to delete:", bg='#b3e0ff').pack(pady=10)
        self.delete_venue_id_entry = tk.Entry(delete_venue_window)
        self.delete_venue_id_entry.pack(pady=5)

        # Button to delete venue
        delete_venue_btn = tk.Button(delete_venue_window, text="Delete Venue", command=self.delete_venue_action, **self.button_style)
        delete_venue_btn.pack(pady=10)

    def delete_venue_action(self):
        venue_id = self.delete_venue_id_entry.get()
        all_venues = Venue.retrieve_all_venues()
        if venue_id:
            if any(venue['venue_id'] == venue_id for venue in all_venues):
                confirm = messagebox.askyesno("Confirm", f"Are you sure you want to delete venue with ID {venue_id}?")
                if confirm:
                    Venue.delete_venue(venue_id)
                    messagebox.showinfo("Success", f"Venue with ID {venue_id} deleted successfully!")
            else:
                messagebox.showerror("Error", f"No venue found with ID {venue_id}.")
        else:
            messagebox.showerror("Error", "Please enter a valid venue ID.")

    # Create a new window for modify venue data
    def modify_venue_data(self):
        modify_venue_window = tk.Toplevel(self.root)
        modify_venue_window.title("Modify Venue Data")
        modify_venue_window.geometry("400x300")
        modify_venue_window.configure(background='#b3e0ff')

        # Label and entry field for venue ID
        tk.Label(modify_venue_window, text="Enter Venue ID to modify:", bg='#b3e0ff').pack(pady=10)
        self.modify_venue_id_entry = tk.Entry(modify_venue_window)
        self.modify_venue_id_entry.pack(pady=5)

        # Button to check venue ID and open modify menu
        check_venue_id_btn = tk.Button(modify_venue_window, text="Check Venue ID", command=self.check_venue_id, **self.button_style)
        check_venue_id_btn.pack(pady=10)

    def check_venue_id(self):
        venue_id = self.modify_venue_id_entry.get()
        all_venues = Venue.retrieve_all_venues()
        individual_venue_data = None
        for venue_data in all_venues:
            if venue_data['venue_id'] == venue_id:
                individual_venue_data = venue_data
                break
        if individual_venue_data:
            self.show_modify_venue_menu(individual_venue_data)
        else:
            messagebox.showerror("Error", f"No venue found with ID {venue_id}.")

    # Create a new window for modify venue data
    def show_modify_venue_menu(self, venue_data):
        modify_venue_window = tk.Toplevel(self.root)
        modify_venue_window.title("Modify Venue Data")
        modify_venue_window.geometry("400x380")
        modify_venue_window.configure(background='#b3e0ff')

        # Labels and entry fields for venue data
        tk.Label(modify_venue_window, text="Venue ID:", bg='#b3e0ff').pack()
        tk.Label(modify_venue_window, text=venue_data['venue_id'], bg='#b3e0ff').pack()

        tk.Label(modify_venue_window, text="Name:", bg='#b3e0ff').pack()
        self.new_name_entry = tk.Entry(modify_venue_window)
        self.new_name_entry.insert(tk.END, venue_data['name'])
        self.new_name_entry.pack()

        tk.Label(modify_venue_window, text="Address:", bg='#b3e0ff').pack()
        self.new_address_entry = tk.Entry(modify_venue_window)
        self.new_address_entry.insert(tk.END, venue_data['address'])
        self.new_address_entry.pack()

        tk.Label(modify_venue_window, text="Contact:", bg='#b3e0ff').pack()
        self.new_contact_entry = tk.Entry(modify_venue_window)
        self.new_contact_entry.insert(tk.END, venue_data['contact'])
        self.new_contact_entry.pack()

        tk.Label(modify_venue_window, text="Min Guests:", bg='#b3e0ff').pack()
        self.new_min_guests_entry = tk.Entry(modify_venue_window)
        self.new_min_guests_entry.insert(tk.END, venue_data['min_guests'])
        self.new_min_guests_entry.pack()

        tk.Label(modify_venue_window, text="Max Guests:", bg='#b3e0ff').pack()
        self.new_max_guests_entry = tk.Entry(modify_venue_window)
        self.new_max_guests_entry.insert(tk.END, venue_data['max_guests'])
        self.new_max_guests_entry.pack()

        # Button to submit modified venue data
        submit_btn = tk.Button(modify_venue_window, text="Submit", command=lambda: self.submit_modified_venue_data(venue_data['venue_id']), **self.button_style)
        submit_btn.pack(pady=10)

    def submit_modified_venue_data(self, venue_id):
        new_name = self.new_name_entry.get()
        new_address = self.new_address_entry.get()
        new_contact = self.new_contact_entry.get()
        new_min_guests = self.new_min_guests_entry.get()
        new_max_guests = self.new_max_guests_entry.get()

        confirm = messagebox.askyesno("Confirm", f"Are you sure you want to modify venue with ID {venue_id}?")
        if confirm:
            # Call the modify method from the Venue class
            Venue.modify(venue_id, new_name, new_address, new_contact, new_min_guests, new_max_guests)
            messagebox.showinfo("Success", f"Venue with ID {venue_id} modified successfully!")

    # Create a new window for display venue data
    def display_all_venue_data(self):
        all_venues = Venue.retrieve_all_venues()
        if all_venues:
            formatted_data = "\n".join([f"Venue ID: {venue['venue_id']}\nName: {venue['name']}\nAddress: {venue['address']}\nContact: {venue['contact']}\nMin Guests: {venue['min_guests']}\nMax Guests: {venue['max_guests']}\n\n" for venue in all_venues])
            self.display_data_window("All Venues", formatted_data)
        else:
            messagebox.showerror("Error", "No venue data found.")

# ************************************************************** Supplier Section **************************************************************

    # Create a new window for Supplier menu
    def open_supplier_menu(self):
        supplier_window = tk.Toplevel(self.root)
        supplier_window.title("Supplier Management")
        supplier_window.geometry("400x300")
        supplier_window.configure(background='#b3e0ff')

        # Add buttons and labels
        add_supplier_btn = tk.Button(supplier_window, text="Add Supplier Data", command=self.add_supplier_data, **self.button_style_submenu)
        add_supplier_btn.pack(pady=10)

        modify_supplier_btn = tk.Button(supplier_window, text="Modify Supplier Data", command=self.modify_supplier_data, **self.button_style_submenu)
        modify_supplier_btn.pack(pady=10)

        display_all_supplier_btn = tk.Button(supplier_window, text="Display All Supplier Data", command=self.display_all_supplier_data, **self.button_style_submenu)
        display_all_supplier_btn.pack(pady=10)

        delete_supplier_btn = tk.Button(supplier_window, text="Delete Supplier Data", command=self.delete_supplier_data, **self.button_style_submenu)
        delete_supplier_btn.pack(pady=10)

    # Create a new window for adding supplier data
    def add_supplier_data(self):
        add_supplier_window = tk.Toplevel(self.root)
        add_supplier_window.title("Add Supplier Data")
        add_supplier_window.geometry("400x350")
        add_supplier_window.configure(background='#b3e0ff')

        # Frame for entries
        entry_frame = tk.Frame(add_supplier_window, bg='#b3e0ff')
        entry_frame.pack(pady=20)

        # Labels and entry fields
        tk.Label(entry_frame, text="Name:", bg='#b3e0ff').grid(row=0, column=0, padx=10, pady=5, sticky="e")
        name_entry = tk.Entry(entry_frame)
        name_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(entry_frame, text="Supplier ID:", bg='#b3e0ff').grid(row=1, column=0, padx=10, pady=5, sticky="e")
        supplier_id_entry = tk.Entry(entry_frame)
        supplier_id_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(entry_frame, text="Address:", bg='#b3e0ff').grid(row=2, column=0, padx=10, pady=5, sticky="e")
        address_entry = tk.Entry(entry_frame)
        address_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(entry_frame, text="Contact Details:", bg='#b3e0ff').grid(row=3, column=0, padx=10, pady=5, sticky="e")
        contact_entry = tk.Entry(entry_frame)
        contact_entry.grid(row=3, column=1, padx=10, pady=5)

        tk.Label(entry_frame, text="Menu:", bg='#b3e0ff').grid(row=4, column=0, padx=10, pady=5, sticky="e")
        menu_entry = tk.Entry(entry_frame)
        menu_entry.grid(row=4, column=1, padx=10, pady=5)

        tk.Label(entry_frame, text="Min Guests:", bg='#b3e0ff').grid(row=5, column=0, padx=10, pady=5, sticky="e")
        min_guests_entry = tk.Entry(entry_frame)
        min_guests_entry.grid(row=5, column=1, padx=10, pady=5)

        tk.Label(entry_frame, text="Max Guests:", bg='#b3e0ff').grid(row=6, column=0, padx=10, pady=5, sticky="e")
        max_guests_entry = tk.Entry(entry_frame)
        max_guests_entry.grid(row=6, column=1, padx=10, pady=5)

        # Add supplier button
        add_supplier_button = tk.Button(add_supplier_window, text="Add Supplier", command=lambda: self.add_supplier_action(name_entry.get(), supplier_id_entry.get(), address_entry.get(), contact_entry.get(), menu_entry.get(), min_guests_entry.get(), max_guests_entry.get()), **self.button_style)
        add_supplier_button.pack(pady=10)

    def add_supplier_action(self, name, supplier_id, address, contact_details, menu, min_guests, max_guests):
        Supplier.add(supplier_id, name, address, contact_details, menu, min_guests, max_guests)
        messagebox.showinfo("Success", "Supplier added successfully!")

    # Create a new window for delete supplier data
    def delete_supplier_data(self):
        delete_supplier_window = tk.Toplevel(self.root)
        delete_supplier_window.title("Delete Supplier")
        delete_supplier_window.geometry("400x200")
        delete_supplier_window.configure(background='#b3e0ff')

        # Label and entry field for supplier ID
        tk.Label(delete_supplier_window, text="Enter Supplier ID to delete:", bg='#b3e0ff').pack(pady=10)
        self.delete_supplier_id_entry = tk.Entry(delete_supplier_window)
        self.delete_supplier_id_entry.pack(pady=5)

        # Button to delete supplier
        delete_supplier_btn = tk.Button(delete_supplier_window, text="Delete Supplier", command=self.delete_supplier_action, **self.button_style)
        delete_supplier_btn.pack(pady=10)

    def delete_supplier_action(self):
        supplier_id = self.delete_supplier_id_entry.get()
        if supplier_id:
            all_suppliers = Supplier.retrieve_all_suppliers()
            if any(supplier['supplier_id'] == supplier_id for supplier in all_suppliers):
                confirm = messagebox.askyesno("Confirm", f"Are you sure you want to delete supplier with ID {supplier_id}?")
                if confirm:
                    Supplier.delete_supplier(supplier_id)
                    messagebox.showinfo("Success", f"Supplier with ID {supplier_id} deleted successfully!")
            else:
                messagebox.showerror("Error", f"No supplier found with ID {supplier_id}.")
        else:
            messagebox.showerror("Error", "Please enter a valid supplier ID.")

    # Create a new window for modify supplier data
    def modify_supplier_data(self):
        modify_supplier_window = tk.Toplevel(self.root)
        modify_supplier_window.title("Modify Supplier Data")
        modify_supplier_window.geometry("400x350")
        modify_supplier_window.configure(background='#b3e0ff')

        # Label and entry field for supplier ID
        tk.Label(modify_supplier_window, text="Enter Supplier ID to modify:", bg='#b3e0ff').pack(pady=10)
        self.modify_supplier_id_entry = tk.Entry(modify_supplier_window)
        self.modify_supplier_id_entry.pack(pady=5)

        # Button to check supplier ID and open modify menu
        check_supplier_id_btn = tk.Button(modify_supplier_window, text="Check Supplier ID", command=self.check_supplier_id, **self.button_style)
        check_supplier_id_btn.pack(pady=10)

    def check_supplier_id(self):
        supplier_id = self.modify_supplier_id_entry.get()
        all_suppliers = Supplier.retrieve_all_suppliers()
        individual_supplier_data = None
        for supplier_data in all_suppliers:
            if supplier_data['supplier_id'] == supplier_id:
                individual_supplier_data = supplier_data
                break
        if individual_supplier_data:
            self.show_modify_supplier_menu(individual_supplier_data)
        else:
            messagebox.showerror("Error", f"No supplier found with ID {supplier_id}.")

    # Create a new window for show modify supplier data
    def show_modify_supplier_menu(self, supplier_data):
        modify_supplier_window = tk.Toplevel(self.root)
        modify_supplier_window.title("Modify Supplier Data")
        modify_supplier_window.geometry("400x300")
        modify_supplier_window.configure(background='#b3e0ff')

        # Frame for entries
        entry_frame = tk.Frame(modify_supplier_window, bg='#b3e0ff')
        entry_frame.pack(pady=20)

        # Labels and entry fields
        tk.Label(entry_frame, text="Name:", bg='#b3e0ff').grid(row=0, column=0, padx=10, pady=5, sticky="e")
        name_entry = tk.Entry(entry_frame)
        name_entry.grid(row=0, column=1, padx=10, pady=5)
        name_entry.insert(0, supplier_data['name'])

        tk.Label(entry_frame, text="Supplier ID:", bg='#b3e0ff').grid(row=1, column=0, padx=10, pady=5, sticky="e")
        supplier_id_entry = tk.Entry(entry_frame)
        supplier_id_entry.grid(row=1, column=1, padx=10, pady=5)
        supplier_id_entry.insert(0, supplier_data['supplier_id'])

        tk.Label(entry_frame, text="Address:", bg='#b3e0ff').grid(row=2, column=0, padx=10, pady=5, sticky="e")
        address_entry = tk.Entry(entry_frame)
        address_entry.grid(row=2, column=1, padx=10, pady=5)
        address_entry.insert(0, supplier_data['address'])

        tk.Label(entry_frame, text="Contact Details:", bg='#b3e0ff').grid(row=3, column=0, padx=10, pady=5, sticky="e")
        contact_entry = tk.Entry(entry_frame)
        contact_entry.grid(row=3, column=1, padx=10, pady=5)
        contact_entry.insert(0, supplier_data['contact_details'])

        tk.Label(entry_frame, text="Menu:", bg='#b3e0ff').grid(row=4, column=0, padx=10, pady=5, sticky="e")
        menu_entry = tk.Entry(entry_frame)
        menu_entry.grid(row=4, column=1, padx=10, pady=5)
        menu_entry.insert(0, supplier_data['menu'])

        tk.Label(entry_frame, text="Min Guests:", bg='#b3e0ff').grid(row=5, column=0, padx=10, pady=5, sticky="e")
        min_guests_entry = tk.Entry(entry_frame)
        min_guests_entry.grid(row=5, column=1, padx=10, pady=5)
        min_guests_entry.insert(0, supplier_data['min_num_of_guest'])

        tk.Label(entry_frame, text="Max Guests:", bg='#b3e0ff').grid(row=6, column=0, padx=10, pady=5, sticky="e")
        max_guests_entry = tk.Entry(entry_frame)
        max_guests_entry.grid(row=6, column=1, padx=10, pady=5)
        max_guests_entry.insert(0, supplier_data['max_num_of_guest'])

        # Modify supplier button
        modify_supplier_button = tk.Button(modify_supplier_window, text="Modify Supplier", command=lambda: self.modify_supplier_action(supplier_data['supplier_id'], name_entry.get(), address_entry.get(), contact_entry.get(), menu_entry.get(), min_guests_entry.get(), max_guests_entry.get()), **self.button_style)
        modify_supplier_button.pack(pady=10)

    def modify_supplier_action(self, supplier_id, name, address, contact_details, menu, min_guests, max_guests):
        Supplier.modify(supplier_id, name, address, contact_details, menu, min_guests, max_guests)
        messagebox.showinfo("Success", "Supplier modified successfully!")

    # Create a new window for display supplier data
    def display_all_supplier_data(self):
        all_suppliers = Supplier.retrieve_all_suppliers()
        if all_suppliers:
            formatted_data = "\n".join([f"Supplier ID: {supplier['supplier_id']}\nName: {supplier['name']}\nAddress: {supplier['address']}\nContact: {supplier['contact_details']}\nMenu: {supplier['menu']}\nMin Guests: {supplier['min_num_of_guest']}\nMax Guests: {supplier['max_num_of_guest']}\n\n" for supplier in all_suppliers])
            self.display_data_window("All Suppliers", formatted_data)
        else:
            messagebox.showerror("Error", "No supplier data found.")

# ************************************************************** Main Section **************************************************************

    def run(self):
        self.root.mainloop()
