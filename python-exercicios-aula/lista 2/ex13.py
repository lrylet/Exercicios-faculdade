'''
13.Faça um programa para multiplicar matrizes 3x3.
'''

matrizA = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
matrizB = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
matrizR = []

print("Cálculo de matriz 3x3\n")
print("Matriz A\n")
for i in range(0,3):
  for j in range(0,3):
    matrizA[i][j] = int(input("Digite os valores da matriz A: "))
print("Matriz B\n")
for k in range(0,3):
  for h in range(0,3):
    matrizB[k][h] = int(input("Digite os valores da matriz B: "))

print(matrizA)
print(matrizB,"\n")

for c in range (0,3):
  matrizRlinha = []
  for l in range (0,3):
    aux = 0
    for m in range (0,3):
      aux += matrizA[c][m] * matrizB[m][l]
    matrizRlinha.append(aux)
  matrizR.append(matrizRlinha)

print("O resultado da multiplicação das matrizes é\n", matrizR)



