#!/bin/bash
# a bash script that send a JSON post request to URL
curl -s --request POST "$1" --data @"$2" -H "Content-Type: application/json"
