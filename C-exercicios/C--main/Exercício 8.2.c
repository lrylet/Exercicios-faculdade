/*Exerc�cio 8.2_1 Escrever um programa que receba do usu�rio um n�mero inteiro positivo, e
que apresente a soma de todos os inteiros positivos pares menores ou iguales que o n�mero
fornecido pelo usu�rio.*/

#include <stdio.h>
#include <locale.h>

int main(){
    setlocale(LC_ALL, "Portuguese");

    float num_usuario;
    float soma;
    int i;

    printf("Digite um n�mero para saber a soma com seus antecessores: ");
    scanf("%f", &num_usuario);
    printf("\n\n");

    for (i = 1; i <= num_usuario; i++){ // a condi��o '<=' � necess�ria para evitar a atribui��o de num_usu�rio para a vari�vel soma
        if (i % 2 == 0) // condi��o para somar apenas os pares
            soma = soma + i;
    }
    printf("A soma dos n�meros antecessores pares de %.f � %.f", num_usuario, soma);

    return 0;
}
 // Leticia Oliveira de Sousa

