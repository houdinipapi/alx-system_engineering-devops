#!/usr/bin/python3

"""
A Python script that returns a given employee information,
about his/her TODO list progress using the REST API.
The script exports data in the CSV format
"""

import json
import requests
import sys
from requests import get
from sys import argv


if __name__ == "__main__":
    # Get employee response
    endpoint = "https://jsonplaceholder.typicode.com"
    user = get(endpoint + "/users/" + argv[1]).json()["username"]

    # Get total number of tasks
    to_dos = get(endpoint + "/todos?userId=" + argv[1]).json()

    record, user_data, group = dict(), dict(), list()
    for to_do in to_dos:
        record["task"] = to_do["title"]
        record["completed"] = to_do["completed"]
        record["username"] = user
        group.append(record)
        record = dict()

    user_data[argv[1]] = group

    # Exporting to JSON
    with open("{}.json".format(argv[1]), "w") as f:
        json.dump(user_data, f)
