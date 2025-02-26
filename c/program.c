#include <stdio.h>

int numberLength(int num, int base){
    int digits = 0;
    while (num!=0) {
        num = num / base;
        digits++;
    }
    return digits;
}

void printMultiplicationTable(int n, char format){
    int i,j;
    for (i=1; i<=n; i++) {
        for (j=1; j<=n; j++) {
            int mnozenie = i*j;
            if (format == 'd'){
                int padding = numberLength(n*n,10)+2;
                printf("%*d", padding, mnozenie);
            }
            else{
                int padding = numberLength(n*n,16)+2;
                printf("%*x", padding, mnozenie);
            }
        }
        printf("\n");
    }
}

int main(int argc, char *argv[]){

    printf("Podaj liczbę n aby wygenerować tabliczkę mnożenia:\n");
    int n;
    scanf("%d", &n);
    if (argc == 1){
        printMultiplicationTable(n,'d');
    }
    else{
        printMultiplicationTable(n,'x');
    }
}
