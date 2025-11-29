#!/usr/bin/python3
"""
Script that fetches employee TODO list progress from a REST API
and displays it in a specific format
"""
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
    employee_name = user_data.get("name")
    
    # Fetch TODO list for the employee
    todos_url = f"{base_url}/todos?userId={employee_id}"
    todos_response = requests.get(todos_url)
    
    if todos_response.status_code != 200:
        sys.exit(1)
    
    todos = todos_response.json()
    
    # Calculate progress
    total_tasks = len(todos)
    completed_tasks = [task for task in todos if task.get("completed")]
    number_of_done_tasks = len(completed_tasks)
    
    # Display results
    print(f"Employee {employee_name} is done with tasks"
          f"({number_of_done_tasks}/{total_tasks}):")
    
    # Display completed task titles
    for task in completed_tasks:
        print(f"\t {task.get('title')}")
