#!/bin/bash
# This script sends a POST request with specified parameters and displays the body of the response
curl -s -X POST -d "email=test@gmail.com" -d "subject=I will always be here for PLD" "$1"
