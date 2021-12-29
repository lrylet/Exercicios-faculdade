'''
10.Escreva um programa que leia um número menor igual a 10 e informe se esse número é primo.
'''
print("Verificador de números primos")
n = int(input("Digite um número de 0 a 10: "))

'''if n > 10:
    print("O número digitado foi maior que 10, tente novamente.")'''

if n >= 0 and n <= 10:
    if n == 1 or n == 2 or n == 3 or n == 5 or n == 7:
        print("\nO número é primo.")
    else:
        print("\nO número não é primo.")
else:
    print("\nO número digitado foi maior que 10, tente novamente.")
    