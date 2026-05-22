#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

int main(){

    char continua;

    double salario;
    double percentual;
    double aumento;
    double novoSalario;

    do{

        system("clear");

        printf("\nDigite o salário: R$");
        scanf("%lf", &salario);

        if(salario <= 280){

            percentual = 20;

        }
        else if(salario <= 700){

            percentual = 15;

        }
        else if(salario <= 1500){

            percentual = 10;

        }
        else{

            percentual = 5;

        }

        aumento = salario * percentual / 100;

        novoSalario = salario + aumento;

        printf("\nSalário antes do reajuste: R$%.2lf\n", salario);
        printf("Percentual aplicado: %.0lf%%\n", percentual);
        printf("Valor do aumento: R$%.2lf\n", aumento);
        printf("Novo salário: R$%.2lf\n", novoSalario);

        printf("\nDeseja continuar (S/N)? ");
        scanf(" %c", &continua);

    }while(toupper(continua) != 'N');

    printf("\nPrograma finalizado.\n");

    return 0;
}
