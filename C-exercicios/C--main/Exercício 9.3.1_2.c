/*
Fazer as alterações necessárias no arquivo fonte ponteirosParaFile2.c
para que o novo programa aceite o nome e 4 notas de cada aluno.
*/
#include <stdio.h>
#include <locale.h>

int main() {

    setlocale(LC_ALL, "Portuguese");

    FILE *arquivop;
    char nome[20];
    float nota1;
    float nota2;
    float nota3;
    float nota4;
    float media;

   if ((arquivop = fopen("turma4notas.txt", "a+")) == NULL) {
      perror("");
      exit(2);
   }

   do {
      fprintf(stderr, "Nome do(a) aluno(a): ");
      fflush(stdin);

      if (fscanf(stdin, "%[^\n]", nome) != 1)
         break;
      fprintf(stderr, "Notas de 4 materias separadas por espaço: ");
      fflush(stdin);
      fscanf(stdin, "%f%f%f%f", &nota1, &nota2, &nota3, &nota4);

      media = (nota1 + nota2 + nota3 + nota4)/4;

      fprintf(arquivop, "%s:%5.2f:%5.2f:%5.2f:%5.2f:%5.2f\n", nome, nota1, nota2, nota3, nota4, media);
   } while (1);

   rewind(arquivop);

   while (fscanf(arquivop, "%[^:]:%f:%f:%f:%f:%f", nome, &nota1, &nota2, &nota3, &nota4, &media) == 6)
      fprintf(stdout, "%-20s %6.2f %6.2f %6.2f %6.2f %6.2f", nome, nota1, nota2, nota3, nota4, media);


    return 0;
}
//Letícia Oliveira de Sousa
