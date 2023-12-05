#!/usr/bin/python3
# AUTH: codenvibes
"""
A Python script that makes a GET request to the URL
"https://alx-intranet.hbtn.io/status", prints information about the
response, including the type, content, and UTF-8 content.
"""
from urllib import request


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"

    with request.urlopen(url) as response:
        body = response.read()
        utf8_content = body.decode("utf-8")

        print("Body response:")
        print("\t- type:", type(body))
        print("\t- content:", body)
        print("\t- utf8 content:", utf8_content)
        response.close()
