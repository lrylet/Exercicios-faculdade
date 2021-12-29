'''
12. Crie um programa para ler duas strings fornecidas pelo
usuário. Verifique se elas foram um anagrama.
'''

a = str(input("Digite uma palavra: ")).lower()
b = str(input("Digite outra palavra: ")).lower()
print("\n O programa verificará se as duas palavras digitadas são um anagrama.")
aOrdenado = sorted(a)
bOrdenado = sorted(b)
#######
if len(a) != len(b):
    print("As palavras possuem tamanhos diferentes. Portanto...")
if sorted(a) == sorted(b):
    print("É um anagrama!")
else:
    print("Não é um anagrama!")