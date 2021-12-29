'''
17.Um motorista de táxi deseja calcular o rendimento de seu carro na praça.
Sabendo-se que o preço do combustível é de R$ 1,90, escreva um programa para ler:
- a marcação do odômetro (Km) no início do dia;
- a marcação (Km) no final do dia;
- o número de litros de combustível gasto;
- e o valor total (R$) recebido dos passageiros.
Calcular e escrever: a média do consumo em Km/L e o lucro (líquido) do dia.
'''

kmInicial = float(input("Digite a marcação do odômetro no início do dia: "))
kmFinal = float(input("Digite a marcação do odômetro no final do dia: "))
kmTotal = kmFinal - kmInicial
combustivelGasto = float(input("Digite o total de litros de combustível gasto durante o dia: "))
valorRecebido = float(input("Digite o valor total recebido dos passageiros: "))
valorCombustivel = combustivelGasto * 1.90
valorTotal = valorRecebido - valorCombustivel

print("O consumo médio, em Km/L, foi de", kmTotal/combustivelGasto, ".\n")
print("O lucro do dia foi de ",valorTotal, "reais.\n")
