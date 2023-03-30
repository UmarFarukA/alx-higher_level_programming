#!/bin/bash
# Scripts that display the size of a request
curl -s "$1" | wc -c
