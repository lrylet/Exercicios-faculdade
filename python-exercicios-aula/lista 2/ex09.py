'''
19.Escreva um programa que leia a idade de 2 homens e 2 mulheres (considere que a idade dos
homens será sempre diferente, assim como as idades das mulheres).
Calcule e escreva a soma das idades do homem mais velho com a mulher mais nova,
e o produto das idades do homem mais novo com a mulher mais velha.
'''

homens = []
mulheres = []

for i in range(2):
    idadeH = int(input("Digite a idade dos homens: "))
    homens.append(idadeH)
homens.sort()

for j in range(2):
    idadeM = int(input("Digite a idade das mulheres: "))
    mulheres.append(idadeM)    
mulheres.sort()

print("Homens: ", homens,"\nMulheres: ",mulheres)

soma = homens[1] + mulheres[0]
mult = homens[0] * mulheres[1]

print("A soma das idades do homem mais velho com a mulher mais nova é de", soma, ". \n")
print("A multiplicação do homem mais novo com a mulher mais velha é de", mult, ".\n")