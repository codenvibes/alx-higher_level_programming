#!/bin/bash
# a Bash script for triggering 'catch_me' endpoint (0.0.0.0:5000/catch_me) and handle server response with 'You got me!'
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
