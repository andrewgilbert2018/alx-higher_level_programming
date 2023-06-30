#!/bin/bash
# a bash script that send a request to a URL pass as an argument
curl -sw "%{http_code}" "$1" -o /dev/null
