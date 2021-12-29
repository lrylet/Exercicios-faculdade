'''
Calcule a área de uma circunferência considerando que o usuário informe
o comprimento do raio. Para essa questão, declare uma variável “pi” com
valor de 3,14 e use como valor de π.
Calcule também o comprimento e o diâmetro.
'''

print("Cálculo de área e comprimento de uma circuferência")

pi = 3.14
raio = int(input("Digite o valor do raio da circuferência: "))
comprimento = 2*pi*raio
area = pi*(raio**2)
print("O comprimento da circuferência é ",comprimento)
print("A área da circuferência é igual a ", area)