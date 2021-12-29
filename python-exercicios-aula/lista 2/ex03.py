'''
3.Escreva um programa para ler valores inteiros
fornecidos pelo usuário e escrevê-los em ordem
crescente.
'''


qtdInserida = int(input('''
Digite uma quantidade de números para organizar
em ordem crescente: '''))

valores = []

for i in range(qtdInserida):
    valor = int(input('Digite um número: '))
    valores.append(valor)
print("Você digitou os seguintes números:\n",valores)
print("")
valores.sort(key=int)
print("A ordem crescente dos números digitados será: ",valores)