'''
Exercício 6:

Faça programas que:
a. Leia um número e imprima o seu quadrado.
b. Leia dois números e imprima a divisão do primeiro pelo segundo.
c. Leia um número e imprima o resto da divisão desse número por 2.
d. Leia dois número e imprima a média.
e. Calcule a área de uma circunferência considerando que o usuário
informe o comprimento do raio.
Para essa questão, declare uma variável “pi” com valor de 3,14
e use como valor de π. Calcule também o comprimento e o diâmetro.
'''

#Letra A
print("============================")
print(" ")

a = int(input("Digite um número inteiro para saber o seu quadrado: "))
print("O quadrado é", a*a)

#Letra B
print("============================")
print(" ")
print("Divisão de dois números")

x = int(input("Digite o primeiro número: "))
y = int(input("Digite o segundo número: "))
print("A divisão do primeiro pelo segundo é: ", x/y)

#Letra C
print("============================")
print(" ")
print("Módulo de divisão")

z = int(input("Digite um número para saber o resto da divisão por 2: "))
print("O resto da divisão é ",z % 2)

#Letra D
print("============================")
print(" ")
print("Cálculo de média")

m = int(input("Digite o primeiro número: "))
n = int(input("Digite o segundo número: "))
print("A média entre esses dois números é ", (m+n)/2)

#Letra E
print("============================")
print(" ")
print("Cálculo de área e comprimento de uma circuferência")

pi = 3.14
raio = int(input("Digite o valor do raio da circuferência: "))
comprimento = 2*pi*raio
area = pi*(raio**2)
print("O comprimento da circuferência é ",comprimento)
print("A área da circuferência é igual a ", area)