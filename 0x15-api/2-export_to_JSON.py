#!/usr/bin/python3
""" script uses REST API for a given employee ID
"""
import json
import requests
import sys


def export_to_json(user_id):
    """ gets TODO list progress for a given employee ID
        Args:
            user_id (int): employee id
    """
    url = 'https://jsonplaceholder.typicode.com/users/'
    employee_url = url + str(user_id)
    employee_response = requests.get(employee_url)
    employee_name = employee_response.json()['name']
    username = employee_response.json()['username']

    todo_url = employee_url + '/todos'
    todos_response = requests.get(todo_url)
    todos = todos_response.json()
    total_tasks = len(todos)
    done_tasks = [task for task in todos if task['completed']]
    number_of_done_tasks = len(done_tasks)

    tasks = []
    for task in todos:
        task_info = {
            "task": task['title'],
            "completed": task['completed'],
            "username": username
        }
        tasks.append(task_info)

    with open(f'{user_id}.json', 'w') as file:
        json.dump({str(user_id): tasks}, file)


if __name__ == "__main__":
    """ run the command
    """
    employee_id = int(sys.argv[1])
    export_to_json(employee_id)
