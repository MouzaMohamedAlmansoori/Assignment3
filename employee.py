# Importing the pickle module for storing data in binay file format
import pickle  

#Class Employee
class Employee:  
    # Constructor method 
    def __init__(self, name, emp_id, department, job_title, basic_salary, age, dob, passport_details, manager_id=None):
        self.name = name  # Assigning employee name
        self.emp_id = emp_id  # Assigning employee ID
        self.department = department  # Assigning employee department
        self.job_title = job_title  # Assigning employee job title
        self.basic_salary = basic_salary  # Assigning employee basic salary
        self.age = age  # Assigning employee age
        self.dob = dob  # Assigning employee date of birth
        self.passport_details = passport_details  # Assigning employee passport details
        self.manager_id = manager_id  # Assigning employee manager ID, default is None

    @staticmethod
    # Method for adding a new employee to the data
    def add(name, emp_id, department, job_title, basic_salary, age, dob, passport_details, manager_id=None):
        # Creating a new employee object
        new_employee = Employee(name, emp_id, department, job_title, basic_salary, age, dob, passport_details, manager_id)
        # Opening file in append binary mode
        with open('employee_binary_data.pkl', 'ab') as file:
            # upate data and writing to file
            pickle.dump(new_employee.__dict__, file)

    @staticmethod
    # Method for retrieving all employees from the data
    def retrieve_all_employees():  
        all_employees = []  # Initialize an empty list for storing employees
        try:  # Try block for handling file operations
            # Opening file in read binary mode
            with open('employee_binary_data.pkl', 'rb') as file:
                while True:  # Loop for reading all employee data from the file
                    try:
                        # load employee data
                        employee_data = pickle.load(file)  
                        # Append employee data to the list
                        all_employees.append(employee_data)  
                    except EOFError:  # Handling end of file
                        break  # Exit loop when end of file is reached
        except FileNotFoundError:  # Handling file not found error
            pass  # Skip if file not found
        return all_employees  # Return the list of all employees

    @staticmethod
    # Method for deleting an employee from the data
    def delete_employee(emp_id):  
        # Retrieve all employees
        employees = Employee.retrieve_all_employees()  
        # Filter out employee to be deleted
        updated_employees = [employee for employee in employees if employee['emp_id'] != emp_id]  
        # Opening file in write binary mode
        with open('employee_binary_data.pkl', 'wb') as file:  
            for employee in updated_employees:  # Loop through updated employee list
                # write updated employee data to file
                pickle.dump(employee, file)  

    @staticmethod
    # Method for modifying individual employee data
    def modify(emp_id, new_name, new_department, new_job_title, new_basic_salary, new_age, new_dob, new_passport_details, new_manager_id=None):
        # Retrieve all employees
        employees = Employee.retrieve_all_employees()  
        for employee in employees:  # Loop through each employee
            if employee['emp_id'] == emp_id:  # Check if employee ID matches the specified ID
                # Update employee attributes
                employee['name'] = new_name  
                employee['department'] = new_department  
                employee['job_title'] = new_job_title  
                employee['basic_salary'] = new_basic_salary  
                employee['age'] = new_age  
                employee['dob'] = new_dob  
                employee['passport_details'] = new_passport_details  
                employee['manager_id'] = new_manager_id  
        # Opening file in write binary mode
        with open('employee_binary_data.pkl', 'wb') as file:  
            for employee in employees:  # Loop through updated employee list
                # write updated employee data to file
                pickle.dump(employee, file)  
