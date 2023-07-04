#!/usr/bin/python3
"""
a Python script that takes 2 arguments in order to solve a challenge
"""
import requests
import sys

if __name__ == "__main__":

    repository = sys.argv[1]
    user = sys.argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(user, repository)
    response = requests.get(url)
    try:
        my_data = response.json()
    except ValueError:
        print("Not a valid JSON")
        exit()
    try:
        if not my_data or my_data.get('message') == "Not Found":
            print("No result")
            exit()
    except AttributeError:
        pass
    for count, commit in enumerate(my_data):
        if count == 10:
            break
        print("{}: {}".format(commit.get('sha'),
                              commit.get('commit').
                              get('author').get('name')))
