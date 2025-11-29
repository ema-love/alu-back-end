#!/usr/bin/python3
"""
Script that exports all employees' TODO list data to JSON format
"""
import json
import requests


if __name__ == "__main__":
    # API base URL
    base_url = "https://jsonplaceholder.typicode.com"
    
    # Fetch all users
    users_url = f"{base_url}/users"
    users_response = requests.get(users_url)
    
    if users_response.status_code != 200:
        exit(1)
    
    users = users_response.json()
    
    # Fetch all todos
    todos_url = f"{base_url}/todos"
    todos_response = requests.get(todos_url)
    
    if todos_response.status_code != 200:
        exit(1)
    
    todos = todos_response.json()
    
    # Create dictionary with user_id as key and username mapping
    user_dict = {user.get("id"): user.get("username") for user in users}
    
    # Organize todos by user
    all_employees_data = {}
    
    for user_id in user_dict.keys():
        user_tasks = []
        
        for task in todos:
            if task.get("userId") == user_id:
                user_tasks.append({
                    "username": user_dict[user_id],
                    "task": task.get("title"),
                    "completed": task.get("completed")
                })
        
        all_employees_data[str(user_id)] = user_tasks
    
    # Export to JSON file
    filename = "todo_all_employees.json"
    
    with open(filename, mode='w') as json_file:
        json.dump(all_employees_data, json_file)
