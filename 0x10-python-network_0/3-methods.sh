#!/bin/bash
# a bash script that take URL and display all the HTTP method
curl -sI "$1" | grep Allow | cut -d ":" -f2| xargs
