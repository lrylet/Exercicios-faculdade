'''
16.Escreva um programa para ler as dimensões de uma cozinha retangular (comprimento, largura e altura),
calcular e escrever a quantidade de caixas de azulejos para se colocar em todas as suas paredes
(considere que não será descontada a área ocupada por portas e janelas).
Cada caixa de azulejos possui 1,5 metros quadrados
'''

comprimento = float(input("Digite o comprimento da cozinha: "))
altura = float(input("Digite a altura da cozinha: "))
area = comprimento * altura
if area % 1.5 != 0:
    totalAzuleijos = (area // 1.5) + 1
else:
    totalAzuleijos = area / 1.5

print("Para uma área de",area,"o total de caixas de azuleijos utilizadas será ",totalAzuleijos, ".")