#!/bin/bash

# List all services that are set to autostart
systemctl list-unit-files --type=service | grep enabled
