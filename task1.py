
# Task 1: Employee Bonus Calculation

# This function calculates the employee bonus.
# The default bonus rate is 10%.
# Extra amounts can be passed using *extras.
# If a cap is provided, the bonus will not exceed that limit.

def bonus(salary, rate=0.1, *extras, **options):
    total_bonus = salary * rate + sum(extras)

    # Apply bonus limit if cap is provided
    if "cap" in options:
        total_bonus = min(total_bonus, options["cap"])

    return total_bonus


# Test the bonus function with sample values
result = bonus(50000, 0.1, 500, 1000, cap=6000)

# Display the calculated bonus
print("Employee Bonus:", result)


# Explanation:
# salary       - Employee salary
# rate=0.1     - Default bonus rate of 10%
# *extras      - Accepts additional bonus amounts
# **options    - Accepts optional keyword arguments
# sum(extras)  - Adds all extra amounts
# min()        - Ensures bonus does not exceed the cap




# Create a custom exception
class InvalidSalaryError(Exception):
    pass


# Create Employee class
class Employee:

    # Initialize employee details
    def __init__(self, name, salary):

        # Check whether salary is negative
        if salary < 0:
            raise InvalidSalaryError(f"Invalid salary: {salary}")

        self.name = name
        self.salary = salary

    # Calculate annual salary
    def annual_salary(self):
        return self.salary * 12



# Create an employee object
employee1 = Employee("Arun", 30000)

# Display employee details
print("Employee Name:", employee1.name)
print("Monthly Salary:", employee1.salary)
print("Annual Salary:", employee1.annual_salary())

# Explanation:
# class Employee  -	Creates an Employee class
# Employee        - Class used to store employee information
# employee1	      - Creates an Employee object
# __init__()      - Initializes name and salary
# self            - Refers to the current employee object
# self.name	      - Stores employee name
# self.salary	  - Stores employee salary
# annual_salary() - Calculates annual salary from monthly salary



# Manager class inherits from Employee
class Manager(Employee):

    # Initialize manager details
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    # Override get_details() to display manager information
    def get_details(self):
        return (
            f"Manager Name: {self.name}\n"
            f"Monthly Salary: {self.salary}\n"
            f"Team Size: {self.team_size}"
        )


# Create a manager object
manager1 = Manager("Priya", 60000, 5)

# Display manager details
print("\nManager Details:")
print(manager1.get_details())


# Explanation:
# Manager(Employee) - Manager inherits properties from Employee
# super().__init__() - Calls the parent class constructor
# team_size - Stores the number of team members
# get_details() - Displays manager information
# Method overriding - Manager provides its own get_details() method


# Understand the Inheritance 
# Employee(Parent Class) name,salary,annual_salary()
#        ->
# Manager (Child Class) team_size,get_details()        


# Test custom exception handling
try:
    employee2 = Employee("Rahul", -500)

except InvalidSalaryError as error:
    print("Error:", error)

finally:
    print("Transaction finished")


# Explanation:
# InvalidSalaryError - Custom exception for invalid salary
# raise - Raises an exception when salary is negative
# try - Executes code that may cause an error
# except - Handles the custom exception
# finally - Executes whether an error occurs or not



# Employee sample data
employees = [
    {"id": 1, "name": "Arun", "department": "Sales", "salary": 30000, "city": "Chennai"},
    {"id": 2, "name": "Priya", "department": "HR", "salary": 45000, "city": "Chennai"},
    {"id": 3, "name": "Rahul", "department": "IT", "salary": 60000, "city": "Bangalore"},
    {"id": 4, "name": "Divya", "department": "IT", "salary": 75000, "city": "Chennai"},
    {"id": 5, "name": "Karthik", "department": "Finance", "salary": 90000, "city": "Mumbai"},
    {"id": 6, "name": "Meena", "department": "Sales", "salary": 52000, "city": "Bangalore"},
    {"id": 7, "name": "Suresh", "department": "IT", "salary": 68000, "city": "Chennai"},
    {"id": 8, "name": "Anitha", "department": "HR", "salary": 48000, "city": "Mumbai"}
]


# Get employee names with salary above 50000
high_salary_names = [
    emp["name"] for emp in employees if emp["salary"] > 50000
]

print("\nAbove 50000:", high_salary_names)


# Add 10% raise to employee salaries using map and lambda
updated_salaries = list(
    map(lambda emp: round(emp["salary"] * 1.10, 2), employees)
)

print("Salaries after 10% raise:", updated_salaries)


# Filter employees who belong to Chennai
chennai_employees = list(
    filter(lambda emp: emp["city"] == "Chennai", employees)
)

# Display Chennai employee names
chennai_names = [emp["name"] for emp in chennai_employees]

print("Chennai:", chennai_names)

# Explanation:
# List comprehension - Creates a list of employees earning above 50000
# map() - Applies a function to every employee salary
# lambda - Creates a small anonymous function
# filter() - Selects employees based on a condition
# list() - Converts the map and filter results into lists



# Loop through employee salaries
print("\nEmployee Salary Loop:")

for emp in employees:

    salary = emp["salary"]

    # Skip employees with salary 0
    if salary == 0:
        continue

    # Stop when salary is above 85000
    if salary > 85000:
        print("Salary above 85000 found:", salary)
        break

    print(emp["name"], "-", salary)


# Explanation:
# for - Iterates through employee records
# continue - Skips the current iteration
# break - Stops the loop completely
# salary == 0 - Checks whether salary is zero
# salary > 85000 - Checks the salary limit
