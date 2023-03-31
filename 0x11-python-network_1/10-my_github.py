#!/usr/bin/python3
"""A scripts that displays users id of github"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    url = "https://api.github.com/user"
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    res = requests.get(url, auth=auth)
    print(res.json().get("id"))
