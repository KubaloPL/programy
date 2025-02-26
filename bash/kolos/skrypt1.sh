#!/bin/bash

#skrypt który przyjmuje dwa argumenty 
# (liczbę i ścieżkę do katalogu) 
# i po prostu je wypisuje o ile ścieżka faktycznie prowadzi do katalogu a nie pliku:

number=$1
path=$2

if [ $number ]; then
    echo $number
else
    echo "Nie podano liczby"
fi

if [[ -d "$path" ]]; then
    echo $path
else
    echo "Podana sciezka nie istnieje"
fi

# przykladowe wykonanie:
# ./skypt1.sh 123 ./

#  123
#  ./
