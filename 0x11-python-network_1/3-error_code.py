#!/usr/bin/python3
"""Scripts that takes and send URL & display response"""
import sys
import urllib.request


if __name__ == "__main__":
    req = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(req) as response:
            content = response.read().decode("ascii")
            print("{}".format(content))
    except HTTPError as e:
        print("Error code: {}".format(e.code))
