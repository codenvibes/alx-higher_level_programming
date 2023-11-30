#!/usr/bin/env bash
# a Bash script to retrieve and display supported HTTP methods for a given URL
curl -Is "$1" | grep Allow | cut -c 8-
