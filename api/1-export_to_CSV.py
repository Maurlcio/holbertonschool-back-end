#!/usr/bin/python3
"""Extracts data about an employee from an API"""
import csv
import json
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
        
        with open(argv[1] + '.csv', 'w') as file:
            for todos in data.json():
                writeobj = csv.writer(file, quoting=csv.QUOTE_ALL)
                writeobj.writerow(
                        [todos['userId'], employee_username,
                        todos['completed'], todos['title']])
    else:
        print("nice try bozo")
