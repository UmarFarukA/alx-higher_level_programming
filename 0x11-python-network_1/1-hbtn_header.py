#!/usr/bin/python3
"""Scripts that takes url and gets X-Request-Id"""
import urllib.request
import sys


if __name__ == "__main__":
    req = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(req) as response:
        print(dict(response.headers).get("X-Request-Id"))
