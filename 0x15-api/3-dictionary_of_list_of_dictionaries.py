#!/usr/bin/python3
""" script uses REST API for a given employee ID
"""
import json
import requests
import sys


def export_to_json():
    """ gets TODO list progress for all employees
    """
    url = 'https://jsonplaceholder.typicode.com/users/'
    users_response = requests.get(url)
    users = users_response.json()

    all_tasks = {}

    for user in users:
        user_id = user['id']
        username = user['username']

        todo_url = url + str(user_id) + '/todos'
        todos_response = requests.get(todo_url)
        todos = todos_response.json()

        tasks = []
        for task in todos:
            task_info = {
                "username": username,
                "task": task['title'],
                "completed": task['completed']
            }
            tasks.append(task_info)

        all_tasks[str(user_id)] = tasks

    with open('todo_all_employees.json', 'w') as file:
        json.dump(all_tasks, file)


if __name__ == "__main__":
    """ run the command
    """
    export_to_json()
