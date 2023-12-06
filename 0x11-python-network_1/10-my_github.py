#!/usr/bin/python3
# AUTH: codenvibes
"""
A script that uses the GitHub API to display the GitHub user ID using
Basic Authentication.

Parameters:
    - username (str): The GitHub username.
    - token (str): The personal access token for authentication
    (with 'read:user' permission).
Usage:
    ./10-my_github.py papamuziko cisfun
"""
import requests
import sys


def get_github_id(username, token):
    url = f'https://api.github.com/user'
    auth = (username, token)
    response = requests.get(url, auth=auth)

    if response.status_code == 200:
        user_data = response.json()
        return user_data.get('id')
    else:
        return None


if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]

    github_id = get_github_id(username, token)

    if github_id is not None:
        print(github_id)
    else:
        print(None)
