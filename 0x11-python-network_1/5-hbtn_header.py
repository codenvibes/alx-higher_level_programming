#!/usr/bin/python3
# AUTH: codenvibes
"""
A Python script that takes in a URL, sends a request to the URL, and
displays the value of the variable `X-Request-Id` in the response header.

Usage:
    ./5-hbtn_header.py <URL>
Parameters:
    url (str): The target URL to send the GET request.
Example:
    ./5-hbtn_header.py https://alx-intranet.hbtn.io
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    response = requests.get(url)
    x_request_id = response.headers.get('X-Request-Id')

    if x_request_id:
        print(x_request_id)
    else:
        print("No X-Request-Id found in the response headers.")
