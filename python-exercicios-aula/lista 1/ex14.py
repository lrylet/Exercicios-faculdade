'''
14.Escreva um programa que leia o valor de 3 ângulos de um triângulo e escreva se o
triângulo é Acutângulo, Retângulo ou Obtusângulo. Sendo que:
- Triângulo Retângulo: possui um ângulo reto. (igual a 90º)
- Triângulo Obtusângulo: possui um ângulo obtuso. (maior que 90º)
- Triângulo Acutângulo: possui três ângulos agudos. (menor que 90º)
'''

def verificador_angulos(a, b, c):
    resposta = ""
    if a < 90 and b < 90 and c < 90:
        resposta = "É um triângulo acutângulo!"
    if a < 90 and b < 90 and c == 90 or a < 90 and b == 90 and c < 90 or a == 90 and b < 90 and c < 90:
        resposta = "É um triângulo retângulo!"
    if a > 90 and b < 90 and c < 90 or a < 90 and b > 90 and c < 90 or a < 90 and b < 90 and c > 90:
        resposta = "É um triângulo obtusângulo!"

    if a + b + c != 180:
        resposta = "A soma dos ângulos internos de um triângulo deve ser igual a 180."
    return resposta

print("Qual é o tipo do triângulo de acordo com os ângulos?\n")

a = int(input("Digite o valor do ângulo a: "))
b = int(input("Digite o valor do ângulo b: "))
c = int(input("Digite o valor do ângulo c: "))

print("\n", verificador_angulos(a, b, c))