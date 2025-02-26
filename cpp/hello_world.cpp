#include <iostream>

using namespace std;


int main(int argc, char *argv[])
{
    char option_char;

    while (true){
        cout << "1. Wypisz ilość argumentów programu" << endl;
        cout << "2. Wypisz wybrany argument programu" << endl;
        cout << "3. Wypisz wszystkie argumenty programu" << endl;
        cout << "4. Zakończ program" << endl;
        cout << "> ";
        cin >> option_char;
        int option_int = option_char - '0';


        switch (option_int){
        case 1:
            cout << "   Ilość argumentów programu: " << argc << endl;
            break;
        case 2:
            cout << "Wybierz argument programu (0 - " << argc-1 <<  "):" << endl;
            cout << "> ";
            int arg;
            cin >> arg;
            if (arg >= 0 && arg < argc){
                cout << arg << endl;
                cout << argv[arg] << endl;
                break;
            }
            else{
                cerr << "   BŁĄD: Nie ma takiego argumentu" << endl;
            }
            break;
        case 3:
            cout << "   Wypisywanie wszystkich argumentów programu:" << endl;
            for ( int i=0; i < argc; i++ ){
                cout << "   argv[" << i << "]: " << argv[i] << endl;
            }
            break;
        case 4:
            return 0;
            break;

        default:
            cerr << "BŁĄD: Podano złą opcje" << end;
        }
    }
}