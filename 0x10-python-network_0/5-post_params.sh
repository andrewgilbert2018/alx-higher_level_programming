#!/bin/bash
# a bash script that take URL and send POST request
curl -s --request POST "$1" -d "email=test@gmail.com&subject=I will always be here for PLD"
