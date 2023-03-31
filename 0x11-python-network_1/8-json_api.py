#!/usr/bin/python3
"""A scripts that send a query parameter to URL"""
import sys
import requests


if __name__ == "__main__":
    term = "" if len(sys.argv) == 1 else sys.argv[1]
    payload = {"q": term}

    res = requests.post("http://0.0.0.0:5000/search_user", data=payload)
    try:
        res = res.json()
        if res == {}:
            print("No result")
        else:
            print("[{}] {}".format(res.get("id"), res.get("name")))
    except ValueError:
        print("Not a valid JSON")
