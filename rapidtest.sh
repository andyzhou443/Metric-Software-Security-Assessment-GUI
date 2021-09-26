#!/usr/bin/bash

# Some technically advanced CI.
# Requires some manual prodding with CTRL-C though.

while true; do
        git fetch && git pull && streamlit run metric.py
done
