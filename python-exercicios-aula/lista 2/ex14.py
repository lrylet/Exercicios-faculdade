'''
Faça um programa para calcular a soma, a subtração e a
multiplicação de matrizes. Você pode fornecer a matriz no
código, em vez de ler o que o usuário digitar,
mas suas funções que fazem os cálculos devem ser
úteis para qualquer tamanho de matriz desde que as
propriedades matemáticas sejam respeitadas.
'''

def podeMultiplicar(a,b):
    retorno = False
    if (len(a) == len(b[0])):
      retorno = True
    return retorno

#####################
def podeSomarSubtr(a, b):
    possivel = False
    if (len(a) == len(b)):
        possivel = True
    return possivel

def multiMatrizes(a,b):
    r = []
    for i in range(len(a)):
        linhaAux = []
        for j in range(len(b[0])):
            aux = 0
            for w in range(len(b)):
                aux += a[i][w]*b[w][j]
            linhaAux.append(aux)
        r.append(linhaAux)
    return r

def somarMatrizes(a,b):
    re = []
    for i in range(len(a)):
        linhaAuxi = []
        auxi = 0
        for j in range(len(b[0])):
            auxi = a[i][j] + b[i][j]
            linhaAuxi.append(auxi)
        re.append(linhaAuxi)
    return re

def subMatrizes(a, b):
    res = []
    for i in range(len(a)):
        linhaAuxiliar = []
        auxiliar = 0
        for j in range(len(b[0])):
            auxiliar = a[i][j] - b[i][j]
            linhaAuxiliar.append(auxiliar)
        res.append(linhaAuxiliar)
    return res


m1 = [[1, 1, 1], [1, 2, 1], [2, 1, 1]]
m2 = [[2, 1, 3], [2, 2, 1], [2, 3, 2]]
if podeMultiplicar(m1, m2):
    print("Multiplicação das matrizes\n", multiMatrizes(m1, m2), "\n")
else:
    print("Não é possível multiplicar essas matrizes.")
if podeSomarSubtr(m1, m2):
    print("Soma das matrizes\n", somarMatrizes(m1, m2), "\n")
    print("Subtração das matrizes\n", subMatrizes(m1, m2), "\n")
else:
    print("Não é possível somar ou subtrair matrizes.")