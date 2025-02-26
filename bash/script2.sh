#!/bin/bash

# Skrypt wypisuje wszystkie pliki
# o zadanym rozszerzeniu znajdujące się
# w bieżącym katalogu i wszystkich jego
# podkatalogach


recursivefind(catalog){
    $0
}

if [ $# -ne 1 ]
then
    echo "Call:"
    echo "progName EXT"
    echo ""
    echo "EXT - extension of the files you want to print out all the file names recursively in all subcatalogs"
else
    # metoda 1:

    # counter=1
    # for v in `find . -name "*$1" | rev | cut -d'/' -f 1 | rev`
    # do
    #     echo "$counter: $v"
    #     counter=$(($counter + 1))
    # done
    # echo ""

    # metoda 2:
    # counter=1
    # for v in `find . -name "*$1" | grep -o '[^/]*$'`
    # do
    #     echo "$counter: $v"
    #     counter=$(($counter + 1))
    # done


fi