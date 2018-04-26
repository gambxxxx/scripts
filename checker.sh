#!/bin/bash
######
    echo "Checking to see if python3 is installed..."
    echo "..."
    sleep 3 
######   
if command -v python3 &>/dev/null; then
    echo "Python 3 is installed"
else
    echo "Python 3 is not installed"
    echo "Press 1 to install "
    read x
    sleep 3
    if [ $x -eq 1 ]; then
        sudo apt-get install python3
    fi
fi
sleep 3
