#!/bin/bash

echo "Enter file/directory name to rest"
read file

if [ -e $file ]
then
    if [ -f $file ]
    then
        echo "$file is a regular file"
    fi
    if [ -d $file ]
    then
        echo "$file is a directory"
    fi
    if [ -r $file ]
    then
        echo "$file is readable"
    fi
    if [ -w $file ]
    then
        echo "$file is writable"
    fi
    if [ -x $file ]
    then
        echo "$file is executable/searchable"
    fi
else
    echo "$file does not exist"
fi