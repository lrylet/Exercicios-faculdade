'''
11.Crie um programa para ler uma string fornecida
pelo usuário. Informe se essa string forma um
palíndromo.
'''

nome = str(input("Digite uma palavra: ")).upper()
palindromo = ""
for i in range(len(nome) - 1, -1, -1): # O primeiro -1 define que o tamanho será 19, o segundo -1 define até qual letra irá o laço e o terceiro -1 significa que voltando uma letra.
    palindromo += nome[i]
print(palindromo, nome)

if palindromo == nome:
    print("A palavra digitada é um palíndromo.")
else:
    print("A palavra digitada não é um palíndromo.")

    #OU

def fpalindromo(a):
    invertido = ""
    resposta = ""
    for j in range(len(a)-1, -1, -1):
        invertido += a[j]
    if invertido == a:
        resposta = "É palíndromo!"
    else:
        resposta = "Não é palíndromo!"
    return resposta

analise = str(input("Digite uma palavra para verificar se é palíndromo: ")).upper()
print(fpalindromo(analise))
