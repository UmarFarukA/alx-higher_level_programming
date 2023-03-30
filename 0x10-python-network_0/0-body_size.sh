#!/bin/bash
#Get the size of a request
curl -s "$1" | wc -c
