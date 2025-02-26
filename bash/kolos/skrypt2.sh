#!/bin/bash

# skrypt który przyjmuje trzy argumenty:
# liczbę (number), 
# ścieżkę do pliku (path_1) 
# i drugą ścieżkę do pliku (path_2).
# W pliku (path_1) powinny być ścieżki, jedna ścieżka w wierszu.
# Skrypt powinien dla każdej ścieżki z pliku wskazanego przez path_1 wykonać następujące wywołanie:
# $ path_2 number path_1

check=true

number=$1
path_1=$2
path_2=$3

if ! [[ $number ]]; then # number
    $check=false
    echo "Nie wpisano liczby w argumencie #1"
fi

if ! [[ -f "$path_1" ]]; then # path_1
    $check=false
    echo "Podana sciezka w argumencie #2 nie jest plikiem"
fi


if ! [[ -d "$path_2" ]]; then # path_2
    $check=false
    echo "Podana sciezka w argumencie #3 nie istnieje"
fi

if [[ $check -eq true ]]; then
    while read line; do
        echo $ $path_2 $number $line
    done < $path_1
fi

# przykladowe wykonanie:
# ./skrypt2.sh 123 ./sciezki.txt /usr

#  $ /usr 123 /usr/
#  $ /usr 123 /bin/


#przy zawartosci pliku sciezki.txt:
#/usr/
#/bin/