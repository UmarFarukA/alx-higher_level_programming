#!/usr/bin/python3
"""A scripts that sends a post request"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    values = {"email": sys.argv[2]}

    response = requests.post(url, data=values)
    print(response.text)
