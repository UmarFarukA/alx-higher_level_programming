#!/bin/bash
# Send a post request to a given url
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
