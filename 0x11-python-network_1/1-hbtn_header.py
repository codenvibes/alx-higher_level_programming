#!/usr/bin/python3
# AUTH: codenvibes
"""
This module retrieves the value of the "X-Request-Id" header from a
specified URL.

Usage:
    python script_name.py <url>
Parameters:
    url (str): The URL from which to fetch the header.
Example:
    ./1-hbtn_header.py https://alx-intranet.hbtn.io
"""
from urllib import request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    with request.urlopen(url) as response:
        header_value = response.getheader("X-Request-Id")
        print(header_value)
        response.close()
