#!/bin/bash

stopped_services=$(systemctl list-units --state=inactive | awk '{print $1}')

echo "Stopped services:"
echo "$stopped_services"
