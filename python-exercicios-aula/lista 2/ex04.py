'''
4.Escreva um programa que leia um número e informe
se esse número é primo.
'''
listaDivisores = []
divisores = 0
numero = int(input("Digite um número para saber se o mesmo é primo: "))
for i in range(1,numero + 1):
    if numero % i == 0:
        listaDivisores.append(i)        
        divisores += 1
if divisores == 2 or divisores == 1:
    print("É primo!")
else:
    print("Não é primo!")
print("É divisível por",listaDivisores)

