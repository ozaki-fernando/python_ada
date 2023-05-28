# WHILE
"""
numero_sorteado = 89
numero_escolhido = int(input ('Informe um número entre 1 e 100: '))

while numero_escolhido != numero_sorteado:
    print ('Você errou! Tente novamente...')
    numero_escolhido = int(input ('Informe um número entre 1 e 100: '))
print ('Parabéns você acertou!')
"""
"""
contador = 0

while contador <= 5:
    print (contador)
    contador = contador + 1
"""
# FOR

'''for variavel in range(10):
    print (variavel)
'''

"""for variavel in range(1, 11):
    print (variavel)"""
'''
for variavel in range(1, 11, 2):
    print (variavel)
'''
soma = 0
for i in range (1, 4):
    nota = float (input (f'Informe sua nota {i}: '))
    soma = soma + nota

print (soma / 3)
