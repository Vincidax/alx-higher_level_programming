#!/bin/bash
# This script sends a JSON POST request with the contents of the specified file and displays the body of the response

file_content=$(cat "$2")
if jq -e . >/dev/null 2>&1 <<<"$file_content"; then
    curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
else
    echo "Not a valid JSON"
fi
