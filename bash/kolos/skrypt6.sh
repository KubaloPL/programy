#!/bin/bash

#skrypt, który dla zadanego katalogu wypisze ścieżki prowadzące do plików znajdujących się w tym katalogu i jego podkatalogach.

check=true

path=$1

if ! [[ -d "$path" ]]; then
    $check=false
    echo "Podana sciezka w argumencie #1 nie istnieje"
fi

if [[ check -eq true ]]; then
    #-type f - upewnia ze wypisuje plik

    for plik in $(find $path -type f); do
        echo $plik
    done
fi

# przykladowe wykonanie:
#./skrypt6.sh ./

    # ./skrypt3.sh
    # ./skrypt2.sh
    # ./test_katalog_2/test.txt
    # ./test_katalog_2/test_2.txt
    # ./skrypt1.sh
    # ./skrypt6.sh
    # ./skrypt5.sh
    # ./test_katalog/test.txt
    # ./test_katalog/test_2.txt
    # ./skrypt4.sh
    # ./skrypt5_dane.json
    # ./sciezki.txt
    # ./plik_json
