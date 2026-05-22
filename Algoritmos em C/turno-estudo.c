#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

int main(){

    char opcao, continua;

    do{

        system("clear");

        printf("Turno de Estudo:");
        printf("\nM - Matutino");
        printf("\nV - Vespertino");
        printf("\nN - Noturno");

        printf("\n\nDigite uma letra: ");
        scanf(" %c", &opcao);

        switch(toupper(opcao)){

            case 'M':
                printf("\nBom Dia!\n");
                break;

            case 'V':
                printf("\nBoa Tarde!\n");
                break;

            case 'N':
                printf("\nBoa Noite!\n");
                break;

            default:
                printf("\nValor Inválido!\n");

        }

        printf("\nDeseja continuar (S/N)? ");
        scanf(" %c", &continua);

    }while(toupper(continua) != 'N');

    printf("\nPrograma finalizado.\n");

    return 0;
}
