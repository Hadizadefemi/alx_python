#!/usr/bin/env python3
"""Takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user 
with the letter as a parameter.
"""


if __name__ == "__main__":
    import sys
    import requests

    letter = sys.argv[1] if len(sys.argv[1]) > 1 else ""
    params = {'q': letter}

    url = "http://0.0.0.0:5000/search_user"
    response = requests.post(url, data=params)

    try:
        data = response.json()
        if data:
            print("[{}] {}".format(data['id'], data['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
