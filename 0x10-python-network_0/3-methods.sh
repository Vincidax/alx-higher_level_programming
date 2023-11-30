#!/bin/bash
# This script displays all HTTP methods accepted by the server for the provided URL
curl -s -I -X OPTIONS "$1" | grep "Allow:" | cut -d' ' -f2-
