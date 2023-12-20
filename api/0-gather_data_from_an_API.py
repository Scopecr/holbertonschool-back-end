#!/usr/bin/python3
"""
data gathering from api module
"""
import requests
import sys


employee_id = sys.argv[1]

user_response = request.get(
    'https://jsonplaceholder.typicode.com/users/' + employee_id)

data = user_response.json()

employee_name = data['name']

todo_response = request.get(
    'https://jsonplaceholder.typicode.com/todos?userId=' + employee_id)

todo_data = todo_response.json()

todo_total = str(len(todo_data))

todo_completed = str(sum(1 for task in todo_data if task['completed']))

print('Employee {} is done with task({}/{}):'.format(employee_name,
                                                     todo_completed, todo_total))

for task in todo_data:
    if task['completed']:
        print('\t {}'.format(task['title']))

if __name__=='__main__':
    pass
