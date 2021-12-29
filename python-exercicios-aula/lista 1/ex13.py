'''
Escreva um programa que leia três entradas numéricas correspondentes às arestas de um triângulos.
Caso os valores permitam que seja formado um triângulo,informe qual tipo de triângulo
(equilátero, isósceles ou escaleno).
'''

def verificador_triangulo(a, b, c):
  resposta = ""
  tipo = ""

  if ((a + b) > c) and ((a + c) > b) and ((c + b) > a):
    resposta = "É um triângulo "
    if a != b and a != c:
        tipo = "escaleno!"
    if a == b and a != c:
        tipo = "isósceles!"
    if a == b and a == c:
        tipo = "equilátero!"
  else:
    resposta = "Não é um triângulo!"
  return resposta + tipo

print ("Digite valores para a, b e c e verifique se formará um triângulo.")

a = int(input("Digite um valor para a: "))
b = int(input("Digite um valor para b: "))
c = int(input("Digite um valor para c: "))

print(verificador_triangulo(a, b, c))