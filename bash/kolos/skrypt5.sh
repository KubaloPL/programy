#!/bin/bash

#skrypt który jako argument przyjmuje ścieżkę prowadzącą do katalogu. 
#Skrypt powinien nazwy wszystkich plików z tego katalogu i ich rozmiary zapisywać w pliku JSON o strukturze:
# {
#   "nazwa_plik_1": <rozmiar_plik_1>,
#   ...,
#   "nazwa_plik_N": <rozmiar_plik_N>
# }

plik_json="skrypt5_dane.json"
check=true

path=$1

if ! [[ -d "$path" ]]; then
    $check=false
    echo "Podana sciezka w argumencie #1 nie istnieje"
fi

if [[ check -eq true ]]; then

    echo "{" > $plik_json
    for plik in $path*; do
        nazwa=$(basename "$plik")
        rozmiar=$(du -sb $nazwa | cut -f1)
        echo '  "'$nazwa'"' :  $rozmiar, >> $plik_json
    done
    truncate -s-2 $plik_json # usuwa 2 ostatnie napisy zeby pozbyć się ostatniego przecinka
    echo "" >> $plik_json
    echo "}" >> $plik_json
    echo "Pomyslnie wykonano program"
fi

# przykladowe wykonanie:
# ./skrypt5.sh ./

#   Pomyslnie wykonano program


# zawartość pliku skrypt5_dane.json po wykonaniu:
# {
#   "plik_json" : 109,
#   "sciezki.txt" : 12,
#   "skrypt1.sh" : 326,
#   "skrypt2.sh" : 928,
#   "skrypt3.sh" : 808,
#   "skrypt4.sh" : 666,
#   "skrypt5_dane.json" : 133,
#   "skrypt5.sh" : 851,
#   "test_katalog" : 0,
#   "test_katalog_2" : 0
# }
