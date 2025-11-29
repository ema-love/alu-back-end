#!/usr/bin/python3
"""
Script that exports employee TODO list data to CSV format
"""
import csv
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)
    
    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        sys.exit(1)
    
    # API base URL
    base_url = "https://jsonplaceholder.typicode.com"
    
    # Fetch employee data
    user_url = f"{base_url}/users/{employee_id}"
    user_response = requests.get(user_url)
    
    if user_response.status_code != 200:
        sys.exit(1)
    
    user_data = user_response.json()
    username = user_data.get("username")
    
    # Fetch TODO list for the employee
    todos_url = f"{base_url}/todos?userId={employee_id}"
    todos_response = requests.get(todos_url)
    
    if todos_response.status_code != 200:
        sys.exit(1)
    
    todos = todos_response.json()
    
    # Export to CSV
    filename = f"{employee_id}.csv"
    
    with open(filename, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        
        for task in todos:
            writer.writerow([
                str(employee_id),
                username,
                str(task.get("completed")),
                task.get("title")
            ])
