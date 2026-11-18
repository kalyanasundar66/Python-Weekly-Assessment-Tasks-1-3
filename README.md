# Task 1 – Python Core, OOP and Errors

## Objective
Develop a Python program to demonstrate Python fundamentals, object-oriented programming, exception handling, and employee data operations.

## Concepts Covered

1. **Functions:** Created a bonus calculation function using default arguments, `*args`, and `**kwargs`.
2. **OOP:** Created an Employee class with an annual salary calculation method.
3. **Inheritance:** Created a Manager class that inherits from Employee and uses `super().__init__()`.
4. **Exception Handling:** Created a custom `InvalidSalaryError` exception to validate negative salaries.
5. **List Comprehension:** Extracted employee names with salaries above 50000.
6. **map() and lambda:** Calculated a 10% salary increase for all employees.
7. **filter():** Selected employees working in Chennai.
8. **Control Flow:** Used `for`, `continue`, and `break` to process employee salaries.

## Sample Results

- Employee bonus: 6000
- Employee annual salary: 360000
- Invalid salary error: Invalid salary: -500
- Employees earning above 50000: Rahul, Divya, Karthik, Meena, Suresh
- Chennai employees: Arun, Priya, Divya, Suresh
- Salary loop stops at the first salary above 85000.

## Files

- `task1.py` – Python implementation of Task 1.
- `README.md` – Project explanation and implementation summary.

## How to Run

```bash
py task1.py
```

## Conclusion

Successfully implemented and tested the required Python concepts using employee sample data.


## Task 2 – CSV, JSON, Environment Variables and API Handling

### Objective
Work with CSV and JSON files, manage environment variables securely, and fetch data from a REST API using Python.

### Requirements Implemented

1. **Virtual Environment and Packages**
   - Created a Python virtual environment.
   - Installed dependencies using `requirements.txt`.
   - Packages: requests, python-dotenv, pandas, matplotlib, numpy.

2. **CSV and JSON File Handling**
   - Read employee records using `csv.DictReader()`.
   - Converted employee records into `employees.json`.
   - Filtered employees earning above ₹50,000.
   - Saved filtered records into `high_earners.csv`.

3. **Environment Variables**
   - Stored `API_KEY` in `.env`.
   - Loaded the key using `python-dotenv`.
   - Retrieved it using `os.getenv()`.
   - Added `.env` and `.venv/` to `.gitignore`.

4. **REST API Handling**
   - Used `requests.get()` to fetch users from JSONPlaceholder.
   - Set a 5-second request timeout.
   - Handled timeout, connection, and HTTP errors.
   - Tested a non-existent user endpoint and handled the 404 response.

5. **Nested JSON Processing**
   - Extracted user ID, name, email, and city.
   - Used `.get()` to safely access nested address information.
   - Saved the extracted records into `users.json`.

### Output Files

| File | Description |
|---|---|
| employees.csv | Original employee data |
| employees.json | Employee data in JSON format |
| high_earners.csv | Employees earning above ₹50,000 |
| users.json | User details retrieved from the API |

### Sample Output

```text
API Key loaded successfully
Rows read: 8 | High earners: 5

First 3 Users:
1 - Leanne Graham - Sincere@april.biz
2 - Ervin Howell - Shanna@melissa.tv
3 - Clementine Bauch - Nathan@yesenia.net

/users/9999 -> 404 Not found
```

### How to Run

```powershell
python -m pip install -r requirements.txt
python task2.py
```

### Conclusion

Successfully implemented CSV and JSON file operations, environment variable management, REST API requests, exception handling, and nested JSON extraction using Python.

## Task 3 – NumPy, Pandas and Matplotlib

### 1. NumPy Operations
- Created a 2D marks array for 4 students and 3 subjects.
- Used `shape` to check array dimensions.
- Calculated student averages using `axis=1`.
- Calculated subject averages using `axis=0`.
- Applied broadcasting to add 5 grace marks.
- Used `np.dot()` to calculate weighted scores.

### 2. Pandas DataFrame Operations
- Loaded employee data from `employees_task3.csv`.
- Used `info()`, `describe()`, `loc`, and `iloc`.
- Filtered employees by department and salary.

### 3. Data Cleaning
- Created `departments.csv` with Sales, HR, IT, Finance, and Marketing.
- Added two missing salary values and one duplicate employee row.
- Filled missing salaries using the median.
- Removed duplicate rows using `drop_duplicates()`.
- Corrected data types.

### 4. Department Analysis and Merging
- Used `groupby().agg()` to calculate department headcount, average salary, and maximum salary.
- Performed inner, left, and outer merges using `pd.merge()`.
- Identified Marketing as the department without employees.

### 5. Matplotlib Visualizations
Created and saved four charts in the `charts/` folder:

1. `bar_average_salary.png` – Average salary by department.
2. `histogram_salary.png` – Salary distribution.
3. `scatter_id_salary.png` – Employee ID vs salary.
4. `line_average_salary.png` – Average salary by department.

### Chart Insights
- Finance has the highest average salary, while Sales has the lowest.
- Most employees have salaries between INR 66,000 and INR 78,000.
- Karthik (Employee ID 5) has the highest salary of INR 90,000.
- Finance has the highest average salary among all departments.

### Files
- `task3.py`
- `employees_task3.csv`
- `departments.csv`
- `charts/`

### Concepts Covered
NumPy, Pandas, DataFrame operations, data cleaning, groupby, aggregation, merging, Matplotlib, and data visualization.