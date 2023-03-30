#!/bin/bash
# Display Allowed HTTP methods of a given server
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
