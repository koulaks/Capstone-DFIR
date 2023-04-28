#!/bin/bash

if [[ $(id -u) -ne 0 ]]; then
   echo "This script must be run as root" 
   exit 1
fi

echo "Open ports:"
netstat -tuln | awk 'NR > 2 {print $4}' | awk -F: '{print $NF}' | sort -n | uniq
