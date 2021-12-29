/*
Fazer as alterações necessárias no arquivo fonte ponteirosParaFile2.c
para que o novo programa aceite o nome e as 3 notas de cada aluno, mas
no lugar da média, o novo programa deve apresentar no final da linha de
reporte, a maior nota do aluno.

*/
#include <stdio.h>
#include <locale.h>

int main(void){

    setlocale(LC_ALL, "Portuguese");

   FILE *arquivop;
   char nome[20];
   float nota1;
   float nota2;
   float nota3;

   if ((arquivop = fopen("turma3notas.txt", "a+")) == NULL) {
      perror("");
      exit(2);
   }

   do {
      fprintf(stderr, "Nome do(a) aluno(a): ");
      fflush(stdin);

      if (fscanf(stdin, "%[^\n]", nome) != 1)
         break;
      fprintf(stderr, "Notas de 3 materias separadas por espaço: ");
      fflush(stdin);
      fscanf(stdin, "%f%f%f", &nota1, &nota2, &nota3);

      if (nota1 > nota2)
        if (nota1 > nota3)
            printf("A maior nota é %f\n",nota1);
        else
            printf("A maior nota é %f\n", nota3);
    else
        if (nota2 > nota3)
            printf("A maior nota é %f\n", nota2);
        else
            printf("A maior nota é %f\n", nota3);

      fprintf(arquivop, "%s:%5.2f:%5.2f:%5.2f\n", nome, nota1, nota2, nota3);
   } while (1);

   rewind(arquivop);

   while (fscanf(arquivop, "%[^:]:%f:%f:%f", nome, &nota1, &nota2, &nota3) == 4)
      fprintf(stdout, "%-20s %6.2f %6.2f %6.2f", nome, nota1, nota2, nota3);

   return(0);
}

// Letícia Oliveira de Sousa
