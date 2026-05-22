#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

int main(){

    char resp;

    system("clear");

    printf("=====================================\n");
    printf(" DESAFIO - CLASSIFICAÇÃO DOS ANIMAIS\n");
    printf("=====================================\n");

    printf("\nPense em um dos animais abaixo:\n");

    printf("\n- Cachorro");
    printf("\n- Gato");
    printf("\n- Leão");
    printf("\n- Elefante");
    printf("\n- Macaco");
    printf("\n- Golfinho");
    printf("\n- Tubarão");
    printf("\n- Águia");
    printf("\n- Pinguim");
    printf("\n- Cobra");
    printf("\n- Jacaré");
    printf("\n- Sapo");
    printf("\n- Galinha\n");

    printf("\nResponda apenas com (S/N)\n");

    // PRIMEIRA PERGUNTA
    printf("\nO animal vive na água? ");
    scanf(" %c", &resp);

    if(toupper(resp) == 'S'){

        // ANIMAIS AQUÁTICOS

        printf("\nO animal é um mamífero? ");
        scanf(" %c", &resp);

        if(toupper(resp) == 'S'){

            printf("\nO animal escolhido foi o GOLFINHO!\n");

        }
        else{

            printf("\nO animal possui dentes afiados? ");
            scanf(" %c", &resp);

            if(toupper(resp) == 'S'){

                printf("\nO animal escolhido foi o TUBARÃO!\n");

            }
            else{

                printf("\nO animal escolhido foi o PINGUIM!\n");

            }

        }

    }
    else{

        // ANIMAIS TERRESTRES / AÉREOS

        printf("\nO animal voa? ");
        scanf(" %c", &resp);

        if(toupper(resp) == 'S'){

            printf("\nO animal caça outros animais? ");
            scanf(" %c", &resp);

            if(toupper(resp) == 'S'){

                printf("\nO animal escolhido foi a ÁGUIA!\n");

            }
            else{

                printf("\nO animal escolhido foi a GALINHA!\n");

            }

        }
        else{

            printf("\nO animal é um réptil? ");
            scanf(" %c", &resp);

            if(toupper(resp) == 'S'){

                printf("\nO animal possui patas? ");
                scanf(" %c", &resp);

                if(toupper(resp) == 'S'){

                    printf("\nO animal escolhido foi o JACARÉ!\n");

                }
                else{

                    printf("\nO animal escolhido foi a COBRA!\n");

                }

            }
            else{

                printf("\nO animal é um mamífero? ");
                scanf(" %c", &resp);

                if(toupper(resp) == 'S'){

                    printf("\nO animal é doméstico? ");
                    scanf(" %c", &resp);

                    if(toupper(resp) == 'S'){

                        printf("\nO animal late? ");
                        scanf(" %c", &resp);

                        if(toupper(resp) == 'S'){

                            printf("\nO animal escolhido foi o CACHORRO!\n");

                        }
                        else{

                            printf("\nO animal escolhido foi o GATO!\n");

                        }

                    }
                    else{

                        printf("\nO animal possui tromba? ");
                        scanf(" %c", &resp);

                        if(toupper(resp) == 'S'){

                            printf("\nO animal escolhido foi o ELEFANTE!\n");

                        }
                        else{

                            printf("\nO animal escolhido foi o LEÃO!\n");

                        }

                    }

                }
                else{

                    printf("\nO animal pula? ");
                    scanf(" %c", &resp);

                    if(toupper(resp) == 'S'){

                        printf("\nO animal escolhido foi o SAPO!\n");

                    }
                    else{

                        printf("\nO animal escolhido foi o MACACO!\n");

                    }

                }

            }

        }

    }

    printf("\n=====================================\n");
    printf(" Programa finalizado.\n");
    printf("=====================================\n");

    return 0;
}
