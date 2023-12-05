#!/usr/bin/python3
# AUTH: codenvibes
"""
A script for sending a POST request to a specified URL with an email parameter.

Parameters:
    url (str): The target URL to which the POST request will be sent.
    email (str): The email parameter to include in the POST request.
Usage:
    ./2-post_email.py <url> <email>
Example:
    ./2-post_email.py http://0.0.0.0:5000/post_email hr@holbertonschool.com
"""
from urllib import request
from urllib import parse
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data = parse.urlencode({"email": email})
    data = data.encode('utf-8')
    req = request.Request(url, data=data, method='POST')

    with request.urlopen(req) as response:
        body = response.read().decode('utf-8')
        print(body)
        response.close()
