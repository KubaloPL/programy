#!/bin/bash

echo "Enter file/directory name to rest"
read file

threshold=90
currentUsage=$(df -h / | grep / | tr - s ' ' | cut -f 5 -d ' ' | tr -d '%')
if [ $currentUsage -ge $threshold ]
then
    echo "Disk space is running low: $currentUsage%""
else
    echo "Disk space is OK: $currentUsage%"
fi