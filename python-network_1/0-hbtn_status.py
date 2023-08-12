#!/usr/bin/env python3
"""This script fetches from a url"""


if __name__ == '__main__':
    import requests
    response = requests.get('https://alu-intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: OK")
