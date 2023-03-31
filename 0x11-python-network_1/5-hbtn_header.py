#!/usr/bin/python3
"""A scripts that display the value of X-Request-Id"""
import sys
import requests


if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    print(response.headers.get("X-Request-Id"))
