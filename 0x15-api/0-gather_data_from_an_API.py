#!/usr/bin/python3
""" script uses REST API for a given employee ID
"""
import requests
import sys


def get_user_todo(user_id):
    """ gets TODO list progress for a given employee ID
        Args:
            user_id (int): employee id
    """
    url = 'https://jsonplaceholder.typicode.com/users/'
    employee_url = url + str(user_id)
    employee_response = requests.get(employee_url)
    employee_name = employee_response.json()['name']

    todo_url = employee_url + '/todos'
    todos_response = requests.get(todo_url)
    todos = todos_response.json()
    total_tasks = len(todos)
    done_tasks = [task for task in todos if task['completed']]
    number_of_done_tasks = len(done_tasks)

    result = f"({number_of_done_tasks}/{total_tasks})"
    first_line = f"Employee {employee_name} is done with tasks{result}:"
    print(first_line)

    for task in done_tasks:
        print(f'\t {task["title"]}')


if __name__ == "__main__":
    """ run the command
    """
    employee_id = int(sys.argv[1])
    get_user_todo(employee_id)
