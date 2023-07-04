#!/usr/bin/python3
"""
a python script that creates request on the internet
"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    address = sys.argv[2]
    dataset = {'email': address}
    response = requests.post(url, data=dataset)
    print(response.text)
