'''
8.Escreva um programa para ler uma temperatura em graus Celsius,
calcular e escrever o valor correspondente em graus Fahrenheit e Kelvin.
'''

c = float(input("Digite uma temperatura para ser convertida para graus Fahrenheit e Kevin: "))
f = ((9 * c ) / 5) + 32
k = (c + 273)

print("A temperatura em Fahrenheit é ",f, ". E em Kelvin é ",k,".")
