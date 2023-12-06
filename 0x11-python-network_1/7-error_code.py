#!/usr/bin/python3
# AUTH: codenvibes
"""
A Python script that sends a GET request to a specified URL and displays
the body of the response.

Parameters:
    url (str): The URL to which the GET request will be sent.
Usage:
    ./7-error_code.py <url>
Example:
    ./7-error_code.py http://0.0.0.0:5000/status_401
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    try:
        response = requests.get(url)
        response.raise_for_status()
        print(response.text)

    except requests.exceptions.HTTPError as err:
        # If there is an HTTP error, print the error code
        print(f"Error code: {err.response.status_code}")
