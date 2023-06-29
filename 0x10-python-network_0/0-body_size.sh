#!/bin/bash
# a bash script that checks url and display the content length
curl -sI "$1" | grep Length | cut -d ' ' -f2
