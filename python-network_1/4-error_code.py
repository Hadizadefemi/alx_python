#!/usr/bin/env python3
"""Takes in a URL, sends a request to the URL and displays the body of the response.
"""


if __name__ == "__main__":
    import sys
    import requests

    url = sys.argv[1]
    re = requests.get(url)

    print(re.text)

    if re.status_code >= 400:
        print("Error code: {}".format(re.status_code))

