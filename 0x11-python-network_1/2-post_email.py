#!/usr/bin/python3
"""A scripts tha sends a post request to url"""
import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    values = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')

    req = urllib.request.Request(url)
    with urllib.request.urlopen(req, data) as response:
        content = response.read().decode("utf-8")
        print("{}".format(content))
