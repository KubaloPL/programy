#!/bin/bash

#skrypt który przyjmuje dwa argumenty:
 #liczbę 
 #ścieżkę do katalogu 
#sprawdza czy łączny rozmiar plików w katalogu (bez podkatalogów) przekracza wartość określoną przez liczbę.

check=true

threshold=$1
path=$2

if ! [[ $threshold ]]; then # liczba
    $check=false
    echo "Nie wpisano liczby w argumencie #1"
fi

if ! [[ -d "$path" ]]; then # sciezka
    $check=false
    echo "Podana sciezka w argumencie #2 nie istnieje"
fi

if [[ check -eq true ]]; then
    rozmiar=$(du -sb $path | cut -f1)
    if [[ $rozmiar -gt $threshold ]]; then
        echo "Rozmiar plikow w katalogu jest wiekszy niz podana wartosc"
    else
        echo "Rozmiar plikow w katalogu jest mniejszy niz podana wartosc"
    fi
fi

# przykladowe wykonanie:
# ./skrypt3.sh 123 ./

#    rozmiar plikow w katalogu jest wiekszy niz podana wartosc
