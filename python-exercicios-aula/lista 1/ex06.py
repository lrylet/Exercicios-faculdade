'''
6. Escreva um programa para ler 3 valores inteiros diferentes e escrevê-los em ordem crescente.
'''

numeros = []

for i in range(3):
    numero = int(input("Digite um número: "))
    numeros.append(numero)
numeros.sort()

print(numeros)
