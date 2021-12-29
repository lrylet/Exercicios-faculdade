'''
9.Faça um programa que leia duas entradas de tipos numéricos.
Verifique qual o maior dos dois ou se eles são iguais.
Imprima uma mensagem informando.
'''
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

if n1 == n2:
    print('Os valores são iguais!')
if n1 > n2:
    print(n1, 'é maior que ',n2)
if n2 > n1:
    print(n2, 'é maior que ',n1)