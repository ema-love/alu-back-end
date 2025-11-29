#!/usr/bin/python3
"""Script to gather employee TODO list progress from API"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(1)
    
    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com"
    
    # Get employee information
    user_response = requests.get(f"{base_url}/users/{employee_id}")
    user_data = user_response.json()
    employee_name = user_data.get("name")
    
    # Get employee's TODO list
    todos_response = requests.get(f"{base_url}/todos?userId={employee_id}")
    todos_data = todos_response.json()
    
    # Calculate completed tasks
    completed_tasks = [task for task in todos_data if task.get("completed")]
    total_tasks = len(todos_data)
    num_completed = len(completed_tasks)
    
    # Display results
    print(f"Employee {employee_name} is done with tasks"
          f"({num_completed}/{total_tasks}):")
    
    for task in completed_tasks:
        print(f"\t {task.get('title')}")
