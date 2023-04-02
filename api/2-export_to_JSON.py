#!/usr/bin/python3
"""Extracts data about an employee from an API"""
from json import dump
from requests import get
from sys import argv

if __name__ == "__main__":
    if argv[1].isdigit() is True:
        employee = get("https://jsonplaceholder.typicode.com/users/{}".format(
                                                                     argv[1]))
        employee_username = employee.json().get('username')

        data = get(
                "https://jsonplaceholder.typicode.com/users/{}/todos".format(
                                                                     argv[1]))

        alltask = {}
        alltask.setdefault(argv[1], [])
        for tasks in data.json():
            alltask[argv[1]].append(dict(
                task=tasks['title'], completed=tasks['completed'],
                username=employee_username))

        with open(argv[1] + '.json', 'w') as file:
            dump(alltask, file)

    else:
        print("nice try bozo")
