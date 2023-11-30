#!/usr/bin/env bash
# a Bash script for GET request to specified URL with X-School-User-Id header set to 98
curl -sH "X-School-User-Id: 98" "$1"
