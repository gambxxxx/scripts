#!/bin/bash
#
# while-menu: a menu driven system information program

DELAY=3 # seconds to display the results

while [[ $REPLY != 0 ]]; do
  clear
  cat <<- _EOF_
      Please select:

      1. Display System information
      2. Display Disk Space
      3. Display Home Space Utilization
      0. Quit
_EOF_

read -p "Enter Selection [0-3] -> "

if [[ $REPLY =~ ^[0-3]$ ]]; then
    if [[ $REPLY == 1 ]]; then
       echo "Hostname: $HOSTNAME"
       uptime
       sleep $DELAY
       continue
    fi
    if [[ $REPLY == 2 ]]; then
       df -h
       sleep $DELAY
       continue
    fi
    if [[ $REPLY == 3 ]]; then
       if [[ $(du -u) -eq 0 ]]; then
          echo "Home Space Utilization (All Users)"
          du -sh /home/*
       else
          echo "Home Space Utiliation ($USER)"
          du -sh $HOME
       fi
       sleep $DELAY
       continue
    fi
    if [[ $REPLY == 0 ]]; then
      break
    fi
else
    echo "Invalid Entry. "
    sleep $DELAY
fi
done
echo "Program terminated."
