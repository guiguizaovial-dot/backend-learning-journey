#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

int main(){

    char continua;

    double lado1, lado2, lado3;

    do{

        system("clear");

        printf("\nDigite o lado 1: ");
        scanf("%lf", &lado1);

        printf("Digite o lado 2: ");
        scanf("%lf", &lado2);

        printf("Digite o lado 3: ");
        scanf("%lf", &lado3);

        if((lado1 + lado2 > lado3) &&
           (lado1 + lado3 > lado2) &&
           (lado2 + lado3 > lado1)){

            printf("\nOs valores formam um triângulo.\n");

            if(lado1 == lado2 && lado2 == lado3){

                printf("Triângulo Equilátero.\n");

            }
            else if(lado1 == lado2 ||
                    lado1 == lado3 ||
                    lado2 == lado3){

                printf("Triângulo Isósceles.\n");

            }
            else{

                printf("Triângulo Escaleno.\n");

            }

        }
        else{

            printf("\nOs valores NÃO formam um triângulo.\n");

        }

        printf("\nDeseja continuar (S/N)? ");
        scanf(" %c", &continua);

    }while(toupper(continua) != 'N');

    printf("\nPrograma finalizado.\n");

    return 0;
}
