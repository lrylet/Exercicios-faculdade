/*A execução do programa de arquivo fonte ponteirosParaFile.c apresenta
uma menságem ao usuário por cada ítem arredondado (“Salvando no
arquivo de saida o item arredondado...”). Para saber o número de itens
considerados, seria necessário contar essas linhas de mensagem. Faça
mudanças no código para que o programa informe automaticamente,
especificamente o número de ítens considerados. */

#include <stdio.h>
#include <locale.h>

int main() {

    setlocale(LC_ALL, "Portuguese");

    FILE *entrada_p;      // ponteiro para o arquivo de entrada
    FILE *saida_p;        // ponteiro para o arquivo de saída

    double item;
    int estado_da_entrada;  // valor do status retornado pela função fscanf

            // Preparação para os arquivos de entrada e saída
    entrada_p = fopen("entrada.txt", "r");
    saida_p   = fopen("saida.txt", "w");

    if (entrada_p == NULL) {
    //Sai do programa caso o arquivo não tenha sido aberto
    printf("Erro ano tentar abrir o arquivo.");
    return 1;

    }
    else {
        int ch = 0;
        int linhas = 0;
        linhas++;

    //Efetua a contagem de linhas lendo o arquivo e procurando a quebra de linha
    while (!feof(entrada_p)) {
      ch = fgetc(entrada_p);

      if (ch == '\n') {
        linhas++;
      }
    }

    // Recebe cada ítem, o formata, e o escreve ao arquivo de saída
    estado_da_entrada = fscanf(entrada_p, "%lf", &item);
    while (estado_da_entrada == 1) {
          fprintf(saida_p, "%.2f\n", item);
          estado_da_entrada = fscanf(entrada_p, "%lf", &item);
    }

    printf("%d linhas foram atualizados em saída.txt.\n",linhas);
    printf("Fechando os arquivos...\n\n");


    //Fecha o arquivo
    fclose(entrada_p);
    fclose(saida_p);

    return 0;

    }
}
