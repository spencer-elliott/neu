#!/bin/bash

# BINF6310
# Module 04 Assignment - Task II
# By Spencer Elliott

top -o COMMAND -b -n 1 > log.txt
sleep 60
top -o COMMAND -b -n 1 >> log.txt
sleep 60
top -o COMMAND -b -n 1 >> log.txt
