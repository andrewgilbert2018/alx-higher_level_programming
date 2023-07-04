#!/usr/bin/python3
"""
a python script that gets information from a url
"""
import requests
import sys

if __name__ == "__main__":

    url = "http://0.0.0.0:5000/search_user"
    if (len(sys.argv) > 1):
        value = sys.argv[1]
    else:
        value = ""
    dataset = {'q': value}
    response = requests.post(url, data=dataset)
    try:
        json = response.json()
        if not json or len(json) == 0:
            print("No result")
        else:
            print("[{}] {}".format(json.get('id'), json.get('name')))
    except ValueError:
        print("Not a valid JSON")
