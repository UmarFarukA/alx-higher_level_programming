#!/usr/bin/python3
"""List of commits of repo sorted in desc"""
import sys
import requests


if __name__ == "__main__":
    url = f"https://api.github.com/repos/{sys.argv[2]}/{sys.argv[1]}/commits"
    res = requests.get(url).json()
    try:
        for j in range(10):
            print("{}: {}".format(res[j].get("sha"),
                                  res[j].get("commit").get("author")
                                  .get("name")))
    except IndexError:
        pass
