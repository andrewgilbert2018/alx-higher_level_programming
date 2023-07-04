#!/usr/bin/python3
"""
a python script that creates request on the internet
"""
from urllib import request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    values = []
    with request.urlopen(url) as response:
        my_data = response.info()
        print(my_data.get("X-Request-Id"))
