'''
11.Faça um programa que leia três entradas de inteiros.
Considere que cada entrada corresponde ao comprimento de uma aresta de um triângulo.
Verifique se os valores passados permitem que seja formado um triângulo considerando
que elas devem se tocar nas extremidades.
'''

def verificador_triangulo(a, b, c):
  resposta = ""

  if ((a + b) > c) and ((a + c) > b) and ((c + b) > a):
    resposta = "É um triângulo!"
  else:
    resposta = "Não é um triângulo!"
  return resposta

print ("Digite valores para a, b e c e verifique se formará um triângulo.")

a = int(input("Digite um valor para a: "))
b = int(input("Digite um valor para b: "))
c = int(input("Digite um valor para c: "))

print(verificador_triangulo(a, b, c))