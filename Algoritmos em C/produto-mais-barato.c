#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

int main(){

    char continua;
    double p1, p2, p3;

    do{

        system("clear");

        printf("\nDigite o preço do produto 1: R$");
        scanf("%lf", &p1);

        printf("Digite o preço do produto 2: R$");
        scanf("%lf", &p2);

        printf("Digite o preço do produto 3: R$");
        scanf("%lf", &p3);

        if(p1 < p2 && p1 < p3){

            printf("\nVocê deve comprar o Produto 1.\n");

        }
        else if(p2 < p1 && p2 < p3){

            printf("\nVocê deve comprar o Produto 2.\n");

        }
        else if(p3 < p1 && p3 < p2){

            printf("\nVocê deve comprar o Produto 3.\n");

        }
        else{

            printf("\nExistem produtos com o mesmo preço.\n");

        }

        printf("\nDeseja continuar (S/N)? ");
        scanf(" %c", &continua);

    }while(toupper(continua) != 'N');

    printf("\nPrograma finalizado.\n");

    return 0;
}
