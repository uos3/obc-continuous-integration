#!/usr/bin/env bash

#check directory for repo specified in README


#run backend script to check commit
python back-end/main.py

# Perform the actual testing separately so it can be called manually for debugging purposes
# if NEW file exists
./test.sh