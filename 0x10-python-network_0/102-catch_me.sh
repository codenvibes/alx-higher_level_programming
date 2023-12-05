#!/bin/bash
# a Bash script for triggering 'catch_me' endpoint (0.0.0.0:5000/catch_me) and handle server response with 'You got me!'
curl -sL -X PUT -H "Origin: HolbertonSchool" -d "user_id=98" 0.0.0.0:5000/catch_me
