#!/bin/bash
# a bash script for sending URL requests and displaying response body size
curl -s "$1" | wc -c
