import matplotlib.pyplot as plt
import os


import numpy as np

# Marks of 4 students in 3 subjects
# Columns: Python, Mathematics, Statistics
marks = np.array([
    [85, 90, 80],
    [75, 80, 85],
    [90, 95, 92],
    [60, 70, 75]
])

# Display the marks array
print("Student Marks:")
print(marks)

# Display array shape
print("\nArray Shape:", marks.shape)

# Calculate each student's average
student_avg = np.mean(marks, axis=1)
print("\nStudent averages:", student_avg)

# Calculate each subject's average
subject_avg = np.mean(marks, axis=0)
print("Subject averages:", subject_avg)

# Add 5 grace marks using broadcasting
grace_marks = marks + 5
print("\nMarks after adding 5 grace marks:")
print(grace_marks)

# Calculate weighted scores
# Weights: Python 40%, Mathematics 35%, Statistics 25%
weights = np.array([0.40, 0.35, 0.25])

weighted_scores = np.dot(marks, weights)
print("\nWeighted scores:", weighted_scores)

# Explanation
# Understand the important NumPy concepts
# Operation	     Meaning
# marks.shape	 Number of rows and columns
# axis=1	     Average across each student's subjects
# axis=0     	 Average across students for each subject
# marks + 5	     Adds 5 to every element using broadcasting
# np.dot()	     Calculates weighted scores


import pandas as pd

# Load employee data using Pandas
df = pd.read_csv("employees_task3.csv")

# Display the first 5 records
print("\nEmployee Data:")
print(df.head())

# Display DataFrame information
print("\nDataFrame Information:")
df.info()

# Display statistical summary
print("\nStatistical Description:")
print(df.describe())

# Select employees using loc
print("\nUsing loc:")
print(df.loc[0:2, ["name", "department", "salary"]])

# Select employees using iloc
print("\nUsing iloc:")
print(df.iloc[0:3, 0:4])

# Filter employees from IT department
print("\nIT Department Employees:")
print(df[df["department"] == "IT"])

# Filter employees earning above 50000
print("\nSalary Above 50000:")
print(df[df["salary"] > 50000])



# Clean the employee dataset

# Check missing salary values
print("\nMissing Salaries Before Cleaning:")
print(df["salary"].isnull().sum())

# Fill missing salaries with the median
median_salary = df["salary"].median()
df["salary"] = df["salary"].fillna(median_salary)

print("\nMedian Salary:", median_salary)

# Remove duplicate records
df = df.drop_duplicates()

# Correct data types
df["id"] = df["id"].astype(int)
df["salary"] = df["salary"].astype(int)

# Reset index after cleaning
df = df.reset_index(drop=True)

# Display cleaned dataset
print("\nCleaned Employee Data:")
print(df)

# Check missing values and duplicates
print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

print("\nDuplicate Rows After Cleaning:")
print(df.duplicated().sum())

print("\nFinal Data Types:")
print(df.dtypes)

print("\nFinal Employee Count:", len(df))



# Department-wise employee analysis using groupby()

department_summary = df.groupby("department").agg(
    headcount=("id", "count"),
    average_salary=("salary", "mean"),
    maximum_salary=("salary", "max")
)

print("\nDepartment Summary:")
print(department_summary)

# Display headcount separately
print("\nDepartment Headcount:")

for department, count in department_summary["headcount"].items():
    print(f"{department}: {count}")

# Identify departments without employees
all_departments = pd.read_csv("departments.csv")

departments_without_employees = all_departments[
    ~all_departments["department"].isin(df["department"])
]

print("\nDepartments Without Employees:")
print(departments_without_employees["department"].tolist())

# Step 7: Pandas Merge Operations

# Inner Merge - Only matching departments
inner_merge = pd.merge(
    df, all_departments,
    on="department",
    how="inner"
)

print("\nInner Merge:")
print(inner_merge)


# Left Merge - All employees with department details
left_merge = pd.merge(
    df, all_departments,
    on="department",
    how="left"
)

print("\nLeft Merge:")
print(left_merge)


# Outer Merge - All employees and all departments
outer_merge = pd.merge(
    df, all_departments,
    on="department",
    how="outer"
)

print("\nOuter Merge:")
print(outer_merge)


# Find departments without employees
print("\nDepartments Without Employees (Outer Join):")

print(
    outer_merge.loc[
        outer_merge["id"].isna(),
        "department"
    ].tolist()
)

# Explanations
# What these merges do
# 1. Inner merge: Displays only matching employee departments.
# 2. Left merge: Keeps all employees and adds department details.
# 3. Outer merge: Includes all employees and all departments, including Marketing.

# Step 8: Matplotlib Charts

# Create charts folder
os.makedirs("charts", exist_ok=True)


# Chart 1: Bar Chart - Average Salary by Department

dept_avg = df.groupby("department")["salary"].mean()

plt.figure(figsize=(8, 5))

plt.bar(
    dept_avg.index,
    dept_avg.values,
    label="Average Salary"
)

plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary (INR)")
plt.legend()

plt.tight_layout()
plt.savefig("charts/bar_average_salary.png")
plt.close()


# Chart 2: Histogram - Salary Distribution

plt.figure(figsize=(8, 5))

plt.hist(
    df["salary"],
    bins=5,
    label="Employee Salaries"
)

plt.title("Salary Distribution")
plt.xlabel("Salary (INR)")
plt.ylabel("Number of Employees")
plt.legend()

plt.tight_layout()
plt.savefig("charts/histogram_salary.png")
plt.close()


# Chart 3: Scatter Plot - Employee ID vs Salary

plt.figure(figsize=(8, 5))

plt.scatter(
    df["id"],
    df["salary"],
    label="Employees"
)

plt.title("Employee ID vs Salary")
plt.xlabel("Employee ID")
plt.ylabel("Salary (INR)")
plt.legend()

plt.tight_layout()
plt.savefig("charts/scatter_id_salary.png")
plt.close()


# Chart 4: Line Chart - Average Salary by Department

plt.figure(figsize=(8, 5))

plt.plot(
    dept_avg.index,
    dept_avg.values,
    marker="o",
    label="Average Salary"
)

plt.title("Average Salary by Department (Line Chart)")
plt.xlabel("Department")
plt.ylabel("Average Salary (INR)")
plt.legend()

plt.tight_layout()
plt.savefig("charts/line_average_salary.png")
plt.close()


print("\nAll four charts saved successfully in the charts folder!")

# Step 9: Chart Insights

print("\nChart Insights:")

print("1. Bar Chart: Finance has the highest average salary, while Sales has the lowest.")

print("2. Histogram: Most employees have salaries between 66000 and 78000.")

print("3. Scatter Plot: Karthik (Employee ID 5) has the highest salary of 90000.")

print("4. Line Chart: Finance has the highest average salary among all departments.")