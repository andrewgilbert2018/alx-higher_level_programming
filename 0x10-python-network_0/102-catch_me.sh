#!/bin/bash
# a bash script that make a request to 0.0.0.0:5000/catch_me
 curl -sL --request PUT 0.0.0.0:5000/catch_me --data "user_id=98" -H "Origin:You find me!"
