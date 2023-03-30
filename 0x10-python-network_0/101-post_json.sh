#!/bin/bash
# A scripts that send JSON POST request to URL
curl -sX POST -H "Content-type: application/json" -d "$(cat "$2")" "$1"
