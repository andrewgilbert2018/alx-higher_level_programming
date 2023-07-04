#!/usr/bin/python3
"""
a Python script that accepts GitHub credentials
"""
import requests
import sys

if __name__ == "__main__":

    url = "https://api.github.com/user"
    user = sys.argv[1]
    one_way_token = sys.argv[2]
    response = requests.get(url, auth=(user, one_way_token))
    my_data = response.json()
    if not my_data:
        print(my_data)
    else:
        print(my_data.get('id'))
