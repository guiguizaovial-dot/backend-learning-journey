#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

int main(){

    char continua;
    double n1, n2, n3, maior, menor;

    do{

        system("clear");

        printf("\nDigite o primeiro número: ");
        scanf("%lf", &n1);

        printf("Digite o segundo número: ");
        scanf("%lf", &n2);

        printf("Digite o terceiro número: ");
        scanf("%lf", &n3);

        maior = n1;

        if(n2 > maior){
            maior = n2;
        }

        if(n3 > maior){
            maior = n3;
        }

        menor = n1;

        if(n2 < menor){
            menor = n2;
        }

        if(n3 < menor){
            menor = n3;
        }

        printf("\nMaior número: %.2lf\n", maior);
        printf("Menor número: %.2lf\n", menor);

        printf("\nDeseja continuar (S/N)? ");
        scanf(" %c", &continua);

    }while(toupper(continua) != 'N');

    printf("\nPrograma finalizado.\n");

    return 0;
}
