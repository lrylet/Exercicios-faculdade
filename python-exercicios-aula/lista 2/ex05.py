'''
5.Escreva um programa para calcular e imprimir o
número de lâmpadas necessárias para iluminar um
determinado cômodo de uma residência.
Dados de entrada: a potência da lâmpada utilizada
(em watts), as dimensões (largura e comprimento,
em metros) do cômodo. Considere que a potência
necessária é de 18 watts por metro quadrado.¹
'''

def iluminação (area, potLampada):
    resposta = ""
    wattsNecessarios =""
    wattsNecessarios = area * 18
    if wattsNecessarios % potLampada != 0:
        resposta = (wattsNecessarios // potLampada) + 1
    else:
        resposta = wattsNecessarios / potLampada
    return resposta



largura = float(input("Digite a largura do cômodo em metros: "))
comprimento = float(input("Digite o comprimento do cômodo em metros: "))
potLampada = float(input("Digite o valor da potência, em watts, da lâmpada que será comprada: "))
area = largura * comprimento

print('\nSerão necessários', iluminação(area,potLampada), 'lâmpadas da potência citada para a iluminação ideal.')