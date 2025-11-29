#!/usr/bin/python3
"""Script to export all employees' TODO lists to JSON format"""
import json
import requests


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com"
    
    # Get all users
    users_response = requests.get(f"{base_url}/users")
    users_data = users_response.json()
    
    # Get all todos
    todos_response = requests.get(f"{base_url}/todos")
    todos_data = todos_response.json()
    
    # Build dictionary of all employees' tasks
    all_tasks = {}
    
    for user in users_data:
        user_id = str(user.get("id"))
        username = user.get("username")
        
        # Filter tasks for this user
        user_tasks = [task for task in todos_data 
                      if task.get("userId") == user.get("id")]
        
        # Build task list for this user
        tasks_list = []
        for task in user_tasks:
            tasks_list.append({
                "username": username,
                "task": task.get("title"),
                "completed": task.get("completed")
            })
        
        all_tasks[user_id] = tasks_list
    
    # Write to JSON file
    filename = "todo_all_employees.json"
    with open(filename, mode='w') as jsonfile:
        json.dump(all_tasks, jsonfile)
