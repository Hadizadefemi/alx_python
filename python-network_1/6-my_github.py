#!/usr/bin/env python3
"""takes your GitHub credentials (username and password) and
uses the GitHub API to display your id
"""


if __name__ == "__main__":
    import requests
    import sys

    username = sys.argv[1]
    password = sys.argv[2]
    url = "https://api.github.com/user"

    response = requests.post(url, auth=(username, password))

    try:
        data = response.json()
        print(data.get('id'))
    except ValueError:
        print("None")
