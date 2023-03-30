#!/bin/bash
# Send a post request to a given url
curl -s -X POST -d "email=test@gmail.com&subject=I will always be there for PLD" "$1"
