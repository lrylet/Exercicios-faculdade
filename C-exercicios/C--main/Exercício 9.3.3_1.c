/*
Refazer o Exercício 9.3.1_4 utilizando a função ordenar do Exemplo
9.3.3_a
*/

#include <stdio.h>
#include <locale.h>

void ordenar(double *menor_p, double *maior_p);

void ordenar(double *menor_p, double *maior_p)    /* entrada/saída */
{
        double temp; /* temporary variable to hold one number during swap      */
        /* Compares values pointed to by smp and lgp and switches if necessary */
         if (*menor_p > *maior_p) {
               temp = *menor_p;
           *menor_p = *maior_p;
           *maior_p = temp;
        }
}


int main(void)
{

    setlocale(LC_ALL, "Portuguese");

   FILE *arquivop;
   char nome[20];
   double nota1;
   double nota2;
   double nota3;

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
      fscanf(stdin, "%lf%lf%lf", &nota1, &nota2, &nota3);

      ordenar(&nota1, &nota2);
      ordenar(&nota1, &nota3);
      ordenar(&nota2, &nota3);

      printf("%.lf %.lf %.lf\n", nota1, nota2, nota3);

      fprintf(arquivop, "%s:%5.2lf:%5.2lf:%5.2lf\n", nome, nota1, nota2, nota3);
   } while (1);

   rewind(arquivop);

   while (fscanf(arquivop, "%[^:]:%lf:%lf:%lf", nome, &nota1, &nota2, &nota3) == 4)
      fprintf(stdout, "%-20s %6.2lf %6.2lf %6.2lf", nome, nota1, nota2, nota3);

   return(0);
}

// Letícia Oliveira de Sousa
