# ESTRUTURAS CONDICIONAIS
'''
idade = 0

idade = int(input ('Digite sua idade: '))

if idade >= 18:
    print ('Sua idade é: ', idade, 'Você é maior de idade!')
else:
    print ('Sua idade é: ', idade, 'Você é não é maior de idade!')
'''

"""
    Imagine que você queira imprimir Aprovada(o), caso o estudante tenha uma média superior
    ou igual a 7, e Reprovado, caso a média seja inferior a 7.
"""
nota1 = 0
nota2 = 0 
media = 0
presenca = 1000
faltas = 0

nota1 = float (input ('Digite a nota da prova B1: '))
nota2 = float (input ('Digite a nota da prova B2: '))
presenca = presenca - (float (input ('Digite o número de faltas: ')) * 100)
media = (nota1 + nota2) / 2

if media >= 7 and presenca > 700:
    print ('Parabéns, sua média foi de: ', media, '. Você está aprovada(o)!')
elif media >= 7 and presenca <699:
    print ('Que pena, sua média foi de: ', media, '. Porém você reprovou por faltas!')
elif media >= 5: #else if
    print ('Que pena, sua média foi de: ', media, '. Você ficou de exame')
else:
    print ('Que pena, sua média foi de: ', media, '. Você está reprovada(o)')