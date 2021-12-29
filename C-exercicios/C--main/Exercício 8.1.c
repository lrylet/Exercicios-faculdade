/*Exercício 8.1_1 Adicione uma nova decisão no código do Exemplo 8.1_b de tal forma que o
programa apresente a mensagem "É a temperatura ambiente ideal!" quando o usuário informe
que sua cidade está em exatamente 24° C.*/

#include <stdio.h>
#include <locale.h>

int main(){
    setlocale(LC_ALL, "Portuguese");

    float temperatura;

    printf("Qual a temperatura na sua cidade hoje?: ");
    scanf("%f",&temperatura);
    printf("\n");

    if(temperatura < 22)
        printf("Agasalhe-se!\n");
    else if (temperatura == 24)
        printf("Uau, temperatura ambiente ideal!");
    else if(temperatura >= 30)
        printf("Calor, hein? Hidrate-se!");
    else
        printf("Dia agradavel! :)");
    printf("\n\n");

    return 0;
}

// Letícia Oliveira de Sousa

