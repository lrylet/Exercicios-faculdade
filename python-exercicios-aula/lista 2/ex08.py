'''
18.Escreva um programa que leia as notas das duas avaliações normais e a nota da avaliação optativa.
Caso o aluno não tenha feito a optativa deve ser fornecido o valor –1.
Calcular a média do semestre considerando que a nota mais baixa será excluída do calculo.
Escrever a média e mensagens que indiquem se o aluno foi aprovado, reprovado ou está em exame,
de acordo com as informações abaixo¹:
Aprovado : media >= 6.0
Reprovado: media < 3.0
Exame : media >= 3.0 e < 6.0
'''
def media_semestre(notas):
    resultado = ""
    media = (notas[0] + notas[1])/2
    if media >= 6.0:
        resultado = 'Aprovado! Sua média é', media
    if media >= 3.0 and media < 6.0:
        resultado = "Exame! Sua média é", media
    if media < 3.0:
        resultado = "Reprovado! Sua média é", media
    return resultado


notas =[]
n1 = float(input("Digite a nota obtida na primeira avaliação: "))
notas.append(n1)
n2 = float(input("Digite a nota obtida na segunda avaliação: "))
notas.append(n2)
op = float(input("Digite a nota obtida na avaliação optativa (caso não tenha feito, digite -1): "))
notas.append(op)
notas.sort()
del(notas[0])

print("As notas que vão entrar na média são: ",notas, "\n")
print(media_semestre(notas))