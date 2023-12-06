#!/usr/bin/python3
# AUTH: codenvibes
"""
A script that sends a POST request to http://0.0.0.0:5000/search_user
with a letter as a parameter.

Usage:
    ./8-json_api.py [letter]

Examples:
    ./8-json_api.py        # No result
    ./8-json_api.py a      # [8446] amnirqhtfjq
    ./8-json_api.py 2      # No result
    ./8-json_api.py b      # [7094] bmofakakhke
"""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        letter = sys.argv[1]
    else:
        letter = ""

    payload = {'q': letter}
    url = 'http://0.0.0.0:5000/search_user'

    try:
        response = requests.post(url, data=payload)
        json_data = response.json()

        if json_data:
            print("[{}] {}".format(json_data.get('id'), json_data.get('name')))
        else:
            print("No result")

    except ValueError:
        print("Not a valid JSON")
