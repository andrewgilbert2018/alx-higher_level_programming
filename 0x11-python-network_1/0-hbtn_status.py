#!/usr/bin/python3
"""
a python script that creates request on the internet
"""
from urllib import request


if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"
    key_values = ['type', 'content', 'utf8 content']
    values = []
    with request.urlopen(url) as response:
        my_data = response.read()
        values.append(type(my_data))
        values.append(my_data)
        values.append(my_data.decode())
        print("Body response:")
        for i in range(3):
            print("\t- {}: {}".format(key_values[i], values[i]))
