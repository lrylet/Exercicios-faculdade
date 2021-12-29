'''
15. Crie um programa que verifica todos os números perfeitos
em um intervalo fornecido pelo usuário. Ou seja, o usuário
fornece dois valores (inicial e final) e o programa verifica se
existe e quais são os números perfeitos nesse intervalo.
Para saber o que são números perfeitos, busque na wikipedia.
'''

print("Digite um intervalo de dois números")

inicio = int(input("Digite o primeiro número do intervalo: "))
fim = int(input("Digite o segundo número do intervalo: "))
for i in range(inicio, fim + 1):
    divisores = 0
    for j in range(1, i):
        if (i % j == 0):
            divisores += j
    if divisores == i:
        print(i, "é um número perfeito!")

