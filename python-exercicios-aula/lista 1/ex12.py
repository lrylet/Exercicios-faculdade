'''
12.Faça um programa para calcular a área de um triângulo.
O usuário deve fornecer os valores da base e da altura.
'''

def area_triangulo(bT, hT):
  return (bT*hT)/2
print("Cálculo de área do triângulo\n")
bT = int(input("Digite o valor da base do triângulo: "))
hT = int(input("Digite o valor da altura do triângulo: "))
print('\n',area_triangulo(bT, hT)," é o valor da área.")