#!/usr/bin/bash

# A technologically revolutionary way to automatically keep pushing changes in our program.
# Requires some manual prodding with CTRL-C though.

while true; do
        git fetch && git pull && streamlit run metric.py
done