#!/bin/bash
"""A scripts that send url and returns size of response"""
curl -s "$1" | wc -c
