import os
from dotenv import load_dotenv
import requests
from requests.exceptions import Timeout, ConnectionError


# Load environment variables from .env
load_dotenv()

# Read API key from environment
api_key = os.getenv("API_KEY")

if api_key:
    print("API Key loaded successfully")
else:
    print("API Key not found")


import csv
import json

# Read employee details from the CSV file
employees = []

with open("employees.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        row["id"] = int(row["id"])
        row["salary"] = int(row["salary"])
        employees.append(row)

# Save all employee details into a JSON file
with open("employees.json", "w", encoding="utf-8") as file:
    json.dump(employees, file, indent=4)

# Find employees whose salary is above 50000
high_earners = [
    emp for emp in employees if emp["salary"] > 50000
]

# Save high earners into a separate CSV file
with open("high_earners.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=employees[0].keys())
    writer.writeheader()
    writer.writerows(high_earners)

# Display the result
print(f"Rows read: {len(employees)} | High earners: {len(high_earners)}")


# Explanation 
# csv.DictReader() reads each employee as a dictionary.
# json.dump() saves all employees into employees.json.
# List comprehension filters salaries above ₹50,000.
# csv.DictWriter() creates high_earners.csv.



# Fetch user details from an API
try:
    response = requests.get(
        "https://jsonplaceholder.typicode.com/users",
        timeout=5
    )

    response.raise_for_status()

    users = response.json()

    print("\nFirst 3 Users:")

    for user in users[:3]:
        print(
            f'{user.get("id")} - '
            f'{user.get("name")} - '
            f'{user.get("email")}'
        )

except Timeout:
    print("Request timed out")

except ConnectionError:
    print("Connection error occurred")

except requests.exceptions.HTTPError as error:
    print("HTTP error:", error)

# Explanation:
# requests.get() sends a GET request.
# timeout=5 limits the wait to 5 seconds.
# response.raise_for_status() detects HTTP errors.
# response.json() converts the API response into Python data.
# users[:3] displays only the first three users.


# Test an API endpoint that does not exist
try:
    response = requests.get(
        "https://jsonplaceholder.typicode.com/users/9999",
        timeout=5
    )

    if response.status_code == 404:
        print("\n/users/9999 -> 404 Not found")
    else:
        response.raise_for_status()

except Timeout:
    print("Request timed out")

except ConnectionError:
    print("Connection error occurred")

except requests.exceptions.HTTPError as error:
    print("HTTP error:", error)

# Explanation:
# /users/9999 requests a user ID that does not exist.
# response.status_code checks the HTTP status.
# 404 means the requested resource was not found.



# Extract selected details from the API response
user_details = []

for user in users:
    details = {
        "id": user.get("id"),
        "name": user.get("name"),
        "email": user.get("email"),
        "city": user.get("address", {}).get("city")
    }

    user_details.append(details)

# Save the extracted details into users.json
with open("users.json", "w", encoding="utf-8") as file:
    json.dump(user_details, file, indent=4)

print("\nUser details saved to users.json")

# Explanation:
# user.get("address", {}) gets the nested address dictionary.
# .get("city") extracts the city safely.
# json.dump() saves the extracted user details into users.json.

