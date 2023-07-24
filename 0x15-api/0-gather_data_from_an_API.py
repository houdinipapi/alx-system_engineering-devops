#!/usr/bin/python3

"""
A Python script that returns a given employee information,
about his/her TODO list progress using the REST API.
"""

import requests
import sys
from sys import argv


if __name__ == "__main__":
    # Get employee response
    endpoint = "https://jsonplaceholder.typicode.com"
    user_response = requests.get(endpoint + "/users/" + argv[1]).json()

    # Get total number of tasks
    to_dos = requests.get(endpoint + "/todos?userId=" + argv[1]).json()

    # Get number of completed tasks and their titles
    tasks_done = [to_do["title"] for to_do in to_dos if to_do["completed"]]

    print("Employee {} is done with tasks({}/{}):"
          .format(user_response["name"], len(tasks_done), len(to_dos)))

    [print("\t {}".format(title)) for title in tasks_done]
