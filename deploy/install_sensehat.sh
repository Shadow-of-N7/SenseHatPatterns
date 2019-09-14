#!/bin/bash

dpkg -s sense-hat &> /dev/null

if [ $? -eq 0 ]; then
    echo "SenseHat driver installed. Starting."
else
    echo "SenseHat driver not installed. Installing..."
	sudo apt-get update
	sudo apt install sense-hat -y
fi