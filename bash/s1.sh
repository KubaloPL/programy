#!/bin/bash

echo "Enter directory name"
read dirName
if [ -d "$dirName" ]
then
    echo "Directory exists"
else
    `mkdir $dirName`
    echo "Directory created"
fi