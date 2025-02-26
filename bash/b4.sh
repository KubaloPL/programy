#!/bin/bash

option=$1

# python:
# if option=="a":
#     [...]
# elif option=="b":
#     [...]
# elif option=="c":
#     [...]
# else:
#     [...]


# C/C++ (idea)
# switch (option){
#     "a":
#         [...]
#         break
#     "b":
#         [...]
#         break
#     "c":
#         [...]
#         break
#     default:
#         [...]
#         break
# }

case ${option} in
    -f) FILE=$2
        echo "File name is $FILE"
        ;& # nie ma break
    -d) DIR=$2
        echo "Directory name is $DIR"
        ;; # jest break
    *)  echo "`basename $0` usage: <-f file_name> | <-d directory_name>"
        exit 1
        ;;
esac