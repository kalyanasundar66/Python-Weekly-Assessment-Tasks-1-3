# Python Weekly Assessment – Tasks 1 to 3

This repository contains the implementation of three weekly Python assessment tasks covering Python fundamentals, Object-Oriented Programming, exception handling, file operations, REST API integration, NumPy, Pandas, data cleaning, and Matplotlib visualizations.

---

# Task 1 – Python Core, OOP and Errors

## 1. Objective

Develop a Python program to demonstrate Python fundamentals, object-oriented programming, exception handling, and employee data operations.

## 2. Concepts Covered

1. **Functions**
   - Created a bonus calculation function.
   - Used default arguments, `*args`, and `**kwargs`.

2. **Object-Oriented Programming (OOP)**
   - Created an `Employee` class.
   - Implemented an annual salary calculation method.

3. **Inheritance**
   - Created a `Manager` class inheriting from `Employee`.
   - Used `super().__init__()` to reuse the parent class constructor.

4. **Exception Handling**
   - Created a custom `InvalidSalaryError` exception.
   - Validated negative salary values.

5. **List Comprehension**
   - Extracted employee names earning above ₹50,000.

6. **map() and lambda**
   - Calculated a 10% salary increase for all employees.

7. **filter()**
   - Selected employees working in Chennai.

8. **Control Flow**
   - Used `for`, `continue`, and `break` to process employee salaries.
   - Stopped the salary loop when the salary exceeded ₹85,000.

## 3. Sample Results

- Employee bonus: 6000
- Employee annual salary: 360000
- Invalid salary error: `Invalid salary: -500`
- Employees earning above ₹50,000: Rahul, Divya, Karthik, Meena, Suresh
- Chennai employees: Arun, Priya, Divya, Suresh
- Salary loop stops at the first salary above ₹85,000.

## 4. Project Files

| File | Description |
|---|---|
| `task1.py` | Python implementation of Task 1 |
| `README.md` | Project explanation and documentation |

## 5. How to Run Task 1

Open PowerShell in the project directory.

```powershell
# Check the installed Python version
py --version

# Create a virtual environment
py -m venv .venv

# Activate the virtual environment
.\.venv\Scripts\Activate.ps1

# Install project dependencies (if requirements.txt exists)
py -m pip install -r requirements.txt

# Execute Task 1
py task1.py
```

## 6. Conclusion

Successfully implemented and tested Python functions, OOP concepts, inheritance, custom exceptions, list comprehension, lambda expressions, map(), filter(), and control flow using employee sample data.

---

# Task 2 – CSV, JSON, Environment Variables and API Handling

## 1. Objective

Work with CSV and JSON files, manage environment variables securely, and retrieve data from a REST API using Python.

## 2. Requirements Implemented

### 2.1 Virtual Environment and Packages

- Created a Python virtual environment.
- Installed dependencies using `requirements.txt`.
- Used the following packages:
  - requests
  - python-dotenv
  - pandas
  - matplotlib
  - numpy

### 2.2 CSV and JSON File Handling

- Read employee records using `csv.DictReader()`.
- Converted employee records into `employees.json`.
- Filtered employees earning above ₹50,000.
- Saved filtered records into `high_earners.csv`.

### 2.3 Environment Variables

- Stored `API_KEY=demo-key-123` in a `.env` file.
- Loaded environment variables using `python-dotenv`.
- Retrieved the API key using `os.getenv()`.
- Added `.env` and `.venv/` to `.gitignore` to prevent sensitive information and virtual environment files from being committed.

### 2.4 REST API Handling

- Used `requests.get()` to retrieve users from JSONPlaceholder.
- Configured a 5-second request timeout.
- Handled timeout, connection, and HTTP errors.
- Tested a non-existent user endpoint.
- Handled the HTTP 404 response.

### 2.5 Nested JSON Processing

- Extracted user ID, name, email, and city.
- Used `.get()` to safely access nested address information.
- Saved extracted user records into `users.json`.

## 3. Output Files

| File | Description |
|---|---|
| `employees.csv` | Original employee data |
| `employees.json` | Employee data converted into JSON |
| `high_earners.csv` | Employees earning above ₹50,000 |
| `users.json` | User details retrieved from the REST API |
| `.env` | Environment variables |
| `.gitignore` | Excludes sensitive and unnecessary files |
| `requirements.txt` | Python package dependencies |

## 4. Sample Output

```text
API Key loaded successfully
Rows read: 8 | High earners: 5

First 3 Users:

1 - Leanne Graham - Sincere@april.biz
2 - Ervin Howell - Shanna@melissa.tv
3 - Clementine Bauch - Nathan@yesenia.net

/users/9999 -> 404 Not found
```

## 5. How to Run Task 2

Open PowerShell in the Task 2 project directory.

```powershell
# Activate the virtual environment
.\.venv\Scripts\Activate.ps1

# Install the required dependencies
py -m pip install -r requirements.txt

# Execute Task 2
py task2.py
```

**Note:** Ensure that the `.env` file is available in the project directory before running the program.

## 6. Conclusion

Successfully implemented CSV and JSON file operations, environment variable management, REST API requests, exception handling, and nested JSON extraction using Python.

---

# Task 3 – NumPy, Pandas and Matplotlib

## 1. Objective

Perform numerical operations, analyze employee datasets, clean data, merge DataFrames, and generate visualizations using NumPy, Pandas, and Matplotlib.

## 2. NumPy Operations

- Created a 2D marks array for 4 students and 3 subjects.
- Used `shape` to check array dimensions.
- Calculated student averages using `axis=1`.
- Calculated subject averages using `axis=0`.
- Applied broadcasting to add 5 grace marks.
- Used `np.dot()` to calculate weighted scores.

## 3. Pandas DataFrame Operations

- Loaded employee data using `employees_task3.csv`.
- Explored the dataset using:
  - `info()`
  - `describe()`
  - `loc`
  - `iloc`
- Filtered employees based on department and salary.

## 4. Data Cleaning

- Created `departments.csv` containing Sales, HR, IT, Finance, and Marketing.
- Introduced two missing salary values and one duplicate employee record.
- Filled missing salary values using the median.
- Removed duplicate records using `drop_duplicates()`.
- Corrected data types.

## 5. Department Analysis and Merging

- Used `groupby().agg()` to calculate:
  - Department headcount.
  - Average salary.
  - Maximum salary.
- Performed different types of DataFrame merges:
  - Inner Join
  - Left Join
  - Outer Join
- Identified Marketing as the department without employees.

## 6. Matplotlib Visualizations

Created and saved four charts in the `charts/` folder.

| Chart | Description |
|---|---|
| `bar_average_salary.png` | Average salary by department |
| `histogram_salary.png` | Salary distribution using a histogram |
| `scatter_id_salary.png` | Employee ID vs. salary |
| `line_average_salary.png` | Average salary by department using a line chart |

### Chart Insights

- Finance has the highest average salary.
- Sales has the lowest average salary.
- Most employees have salaries between ₹66,000 and ₹78,000.
- Karthik (Employee ID 5) has the highest salary of ₹90,000.
- Finance has the highest average salary among all departments.

## 7. Project Files

| File / Folder | Description |
|---|---|
| `task3.py` | Python implementation of Task 3 |
| `employees_task3.csv` | Employee dataset |
| `departments.csv` | Department dataset |
| `charts/` | Folder containing generated visualizations |

## 8. How to Run Task 3

Open PowerShell or the VS Code terminal in the Task 3 project directory.

### Step 1: Activate the Virtual Environment

```powershell
# Activate the existing virtual environment
.\.venv\Scripts\Activate.ps1
```

### Step 2: Install Required Libraries

```powershell
# Install NumPy, Pandas and Matplotlib
py -m pip install numpy pandas matplotlib
```

### Step 3: Execute the Python Program

```powershell
# Run Task 3
py task3.py
```

This executes:

1. NumPy array operations.
2. Pandas DataFrame analysis.
3. Data cleaning and preprocessing.
4. Department grouping and aggregation.
5. Inner, left, and outer merges.
6. Matplotlib visualizations.

### Step 4: Verify Generated Charts

After successful execution, check the `charts/` directory.

```text
charts/
│
├── bar_average_salary.png
├── histogram_salary.png
├── scatter_id_salary.png
└── line_average_salary.png
```

### Step 5: Regenerate the Charts

Run the script again whenever you want to regenerate the visualizations.

```powershell
# Re-execute the script to regenerate all charts
py task3.py
```

**Note:** Run the commands from the directory containing `task3.py` and the required CSV files.

## 9. Concepts Covered

- NumPy arrays and mathematical operations.
- Pandas DataFrame manipulation.
- Data exploration and filtering.
- Missing value handling.
- Duplicate removal.
- Data type conversion.
- GroupBy and aggregation.
- DataFrame merging.
- Matplotlib data visualization.

## 10. Conclusion

Successfully implemented numerical operations using NumPy, employee data analysis using Pandas, data cleaning, department-level analysis, DataFrame merging, and data visualization using Matplotlib.

---

# Overall Assessment Conclusion

Successfully completed all three Python weekly assessment tasks.

The assessment demonstrates practical knowledge of Python programming, object-oriented programming, exception handling, file handling, API integration, environment variable management, numerical computing, data analysis, data cleaning, and visualization.

**Technologies and Libraries Used:**

- Python
- NumPy
- Pandas
- Matplotlib
- Requests
- Python-dotenv
- CSV and JSON
- REST API

**Assessment Tasks Completed:**

1. Python Core, OOP and Errors
2. CSV, JSON, Environment Variables and API Handling
3. NumPy, Pandas and Matplotlib

**Status:** Successfully implemented and tested the three assessment tasks.
