#!/bin/bash
# a Bash script for POST request with specified variables (email, subject)
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
