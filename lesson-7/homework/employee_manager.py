class Employee:
    def __init__(self, employee_id, name, position, salary):
        """Initialize an Employee object with ID, name, position, and salary."""
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary

    def __repr__(self):
        """Return a string representation of the Employee object."""
        return f"Employee(ID: {self.employee_id}, Name: {self.name}, Position: {self.position}, Salary: {self.salary})"
    
    def __str__(self):
        """Return a user-friendly string representation of the Employee."""
        return f"{self.employee_id}, {self.name}, {self.position}, {self.salary}"

class EmployeeManager:
    FILE_NAME = "employees.txt"
    
    @staticmethod
    def add_employee():
        """Add a new employee to the file."""
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Name: ")
        position = input("Enter Position: ")
        salary = input("Enter Salary: ")
        emp = Employee(emp_id, name, position, salary)
        with open(EmployeeManager.FILE_NAME, "a") as file:
            file.write(str(emp) + "\n")
        print("Employee added successfully!")
    
    @staticmethod
    def view_all_employees():
        """View all employee records from the file."""
        try:
            with open(EmployeeManager.FILE_NAME, "r") as file:
                employees = file.readlines()
                if not employees:
                    print("No employee records found.")
                else:
                    print("Employee Records:")
                    for emp in employees:
                        print(emp.strip())
        except FileNotFoundError:
            print("No employee records found.")
    
    @staticmethod
    def search_employee():
        """Search for an employee by Employee ID and display details."""
        emp_id = input("Enter Employee ID to search: ")
        try:
            with open(EmployeeManager.FILE_NAME, "r") as file:
                for line in file:
                    data = line.strip().split(", ")
                    if data[0] == emp_id:
                        print("Employee Found:")
                        print(", ".join(data))
                        return
            print("Employee not found.")
        except FileNotFoundError:
            print("No employee records found.")
    
    @staticmethod
    def update_employee():
        """Update an employee's information."""
        emp_id = input("Enter Employee ID to update: ")
        try:
            with open(EmployeeManager.FILE_NAME, "r") as file:
                employees = file.readlines()
            
            updated_employees = []
            found = False
            for line in employees:
                data = line.strip().split(", ")
                if data[0] == emp_id:
                    found = True
                    name = input("Enter new Name (leave blank to keep current): ") or data[1]
                    position = input("Enter new Position (leave blank to keep current): ") or data[2]
                    salary = input("Enter new Salary (leave blank to keep current): ") or data[3]
                    updated_employees.append(f"{emp_id}, {name}, {position}, {salary}\n")
                else:
                    updated_employees.append(line)
            
            if found:
                with open(EmployeeManager.FILE_NAME, "w") as file:
                    file.writelines(updated_employees)
                print("Employee record updated successfully!")
            else:
                print("Employee not found.")
        except FileNotFoundError:
            print("No employee records found.")
    
    @staticmethod
    def delete_employee():
        """Delete an employee record."""
        emp_id = input("Enter Employee ID to delete: ")
        try:
            with open(EmployeeManager.FILE_NAME, "r") as file:
                employees = file.readlines()
            
            updated_employees = [line for line in employees if not line.startswith(emp_id + ", ")]
            
            if len(updated_employees) < len(employees):
                with open(EmployeeManager.FILE_NAME, "w") as file:
                    file.writelines(updated_employees)
                print("Employee record deleted successfully!")
            else:
                print("Employee not found.")
        except FileNotFoundError:
            print("No employee records found.")
    
    @staticmethod
    def menu():
        while True:
            print("\nWelcome to the Employee Records Manager!")
            print("1. Add new employee record")
            print("2. View all employee records")
            print("3. Search for an employee by Employee ID")
            print("4. Update an employee's information")
            print("5. Delete an employee record")
            print("6. Exit")
            choice = input("Enter your choice: ")
            
            if choice == "1":
                EmployeeManager.add_employee()
            elif choice == "2":
                EmployeeManager.view_all_employees()
            elif choice == "3":
                EmployeeManager.search_employee()
            elif choice == "4":
                EmployeeManager.update_employee()
            elif choice == "5":
                EmployeeManager.delete_employee()
            elif choice == "6":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

# Run the Employee Manager menu
EmployeeManager.menu()
