#!/usr/bin/python3

"""
A Python script that returns a given employee information,
about his/her TODO list progress using the REST API.
The script exports data in the CSV format
"""

import csv
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

    # Exporting data in the CSV format
    with open("{}.csv".format(argv[1]), "w") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for to_do in to_dos:
            writer.writerow([argv[1], user, to_do["completed"],
                             to_do["title"]])
