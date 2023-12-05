#!/usr/bin/python3
# AUTH: codenvibes
"""
A script to fetch and print the content of a URL.

Parameters:
    url (str): The URL whose content will be fetched and printed.
Usage:
    python script.py <url>
"""


from urllib import request, error
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with request.urlopen(url) as response:
            body = response.read().decode('utf-8')
            print(body)
    except error.HTTPError as e:
        print(f"Error code: {e.code}")
