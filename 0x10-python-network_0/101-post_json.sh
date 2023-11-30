#!/bin/bash
# This script sends a JSON POST request with the contents of the specified file and displays the body of the response
# Check if URL and JSON file are provided
if [ -z "$1" ] || [ -z "$2" ]; then
    echo "Please provide a URL and a JSON file"
    exit 1
fi

# Check if JSON file is valid
if ! jq '.' "$2" > /dev/null 2>&1; then
    echo "Not a valid JSON"
    exit 1
fi

# Send POST request with contents of JSON file in the body
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"
