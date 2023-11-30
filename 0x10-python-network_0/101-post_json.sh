#!/bin/bash
# This script sends a JSON POST request with the contents of the specified file and displays the body of the response
if jq -e . "$2" >/dev/null 2>&1; then curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"; else echo "Not a valid JSON"; fi
