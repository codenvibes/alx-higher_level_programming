#!/usr/bin/python3
# AUTH: codenvibes
"""
A script that sends a POST request to a specified URL with an email parameter.

Parameters:
    url (str): The target URL to which the POST request will be sent.
    email (str): The email parameter to include in the POST request.
Usage:
    ./6-post_email.py <url> <email>
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = {"email": email}
    response = requests.post(url, data=data)

    print(response.text)
