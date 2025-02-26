#!/bin/bash

# skrypt który przyjmuje dwa argumenty: 
 #ścieżkę do pliku (path_1) 
 #drugą ścieżkę do pliku (path_2). 
#Skrypt powinien wszystkie pliki z katalogu wskazanego przez path_1 skopiować do katalogu wskazanego przez path_2.

check=true

path_1=$1
path_2=$2

if ! [[ -d "$path_1" ]]; then
    $check=false
    echo "Podana sciezka w argumencie #1 nie istnieje"
fi

if ! [[ -d "$path_2" ]]; then
    $check=false
    echo "Podana sciezka w argumencie #2 nie istnieje"
fi

if [[ check -eq true ]]; then
    cp $path_1/* $path_2
    echo "Pomyslnie wykonano program"
fi

# przykladowe wykonanie:
# ./skrypt4.sh ./test_katalog ./test_katalog_2

#   Pomyślnie wykonano program
