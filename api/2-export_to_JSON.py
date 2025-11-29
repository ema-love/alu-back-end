#!/usr/bin/python3
"""
Script that exports employee TODO list data to JSON format
"""
import json
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
    
    # Prepare data for JSON export
    tasks_list = []
    for task in todos:
        tasks_list.append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        })
    
    # Create JSON structure
    json_data = {str(employee_id): tasks_list}
    
    # Export to JSON file
    filename = f"{employee_id}.json"
    
    with open(filename, mode='w') as json_file:
        json.dump(json_data, json_file)
