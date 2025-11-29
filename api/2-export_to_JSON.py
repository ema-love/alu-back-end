#!/usr/bin/python3
"""Script to export employee TODO list to JSON format"""
import json
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
    username = user_data.get("username")
    
    # Get employee's TODO list
    todos_response = requests.get(f"{base_url}/todos?userId={employee_id}")
    todos_data = todos_response.json()
    
    # Build JSON structure
    tasks_list = []
    for task in todos_data:
        tasks_list.append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        })
    
    json_data = {employee_id: tasks_list}
    
    # Write to JSON file
    filename = f"{employee_id}.json"
    with open(filename, mode='w') as jsonfile:
        json.dump(json_data, jsonfile)
