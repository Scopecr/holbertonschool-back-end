#!/usr/bin/python3
"""Script to return info about todo list progress"""
import requests
from sys import argv


def information_employee():
    """Returns information about employees"""
    if len(argv) != 2:
        print("Usage: {} <employee_id>".format(argv[0]))
        return

    id_employee = int(argv[1])
    employee_name = ""
    number_of_done_tasks = 0
    total_number_of_tasks = 0
    task_titles = []

    url_users = 'https://jsonplaceholder.typicode.com/users'
    url_todos = 'https://jsonplaceholder.typicode.com/todos'

    # Get user data
    user_url = f"https://jsonplaceholder.typicode.com/users/{id_employee}"
    user_response = requests.get(user_url)

    if user_response.status_code != 200:
        print("Error: Unable to fetch user data. Status code: {}".format(user_response.status_code))
        return

    user_data = user_response.json()
    employee_name = user_data['name']

    # Get todos data
    todos_response = requests.get(url_todos)

    if todos_response.status_code != 200:
        print("Error: Unable to fetch todos data. Status code: {}".format(todos_response.status_code))
        return

    todos_data = todos_response.json()

    for todo in todos_data:
        if todo['userId'] == id_employee:
            total_number_of_tasks += 1
            if todo['completed']:
                number_of_done_tasks += 1
                task_titles.append(todo['title'])

    print('Employee {} is done with tasks ({}/{}):'
          .format(employee_name, number_of_done_tasks, total_number_of_tasks))
    
    for title in task_titles:
        print('\t{}'.format(title))


if __name__ == "__main__":
    information_employee()
