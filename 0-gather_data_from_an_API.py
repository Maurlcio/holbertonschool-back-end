#!/usr/bin/python3
"""Extracts data about an employee from an API"""
from requests import get
from sys import argv
import json

if __name__ == "__main__":
    if argv[1].isdigit() is True:
        employee = get("https://jsonplaceholder.typicode.com/users/{}".format(
                                                                     argv[1]))
        employee_name = employee.json().get('name')

        data = get(
                "https://jsonplaceholder.typicode.com/users/{}/todos".format(
                                                                     argv[1]))
        done_tasks = []
        for todos in data.json():
            if todos['completed'] is True:
                done_tasks.append(todos['title'])
        done_tasks_len = len(done_tasks)
        total_tasks = len(data.json())

        print("Employee {} is done with tasks({}/{}):".format(employee_name,
                                                              done_tasks_len,
                                                              total_tasks))
        for todone in done_tasks:
            print("\t {}".format(todone))
    else:
        print("nice try bozo")
