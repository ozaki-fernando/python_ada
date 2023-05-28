# FUNÇÕES

#Criando funções
#Função inicial
'''
def saudacao():
    print('Seja bem-vinda(o)!')
    print('Olá, é um prazer ter você fazendo parte desse curso!')

saudacao()
'''

# Função com parâmetros
'''
def saudacao(nome, curso):
    print(f'Seja bem-vinda(o)! {nome}')
    print(f'Olá, é um prazer ter você fazendo parte do curso de {curso}!')

saudacao(input('Digite seu nome: '), input('Digite o nome do curso: '))
'''
#Função com parâmetros default
'''
def saudacao(nome, curso = 'Python'):
    print(f'Seja bem-vinda(o)! {nome}')
    print(f'Olá, é um prazer ter você fazendo parte do curso de {curso}!')

saudacao(input('Digite seu nome: '))
'''

# Funções com retorno
'''def soma (num1, num2):
    return num1 + num2

resultado = soma (5,7)

print(f'O resultado da soma é: {resultado}')'''

def calculadora (num1, num2, op):
    if op == '+':
        print('Você escolheu somar!')
        return num1 + num2
    elif op == '-':
        print('Você escolheu subtrair!')
        return num1 - num2
    elif op == '*':
        print('Você escolheu multiplicar!')
        return num1 * num2
    else:
        print('Você escolheu dividir!')
        return num1 / num2

num1 = float(input('Digite o primeiro número: '))
op = str(input('Digite a operação desejada: '))
num2 = float(input('Digite o primeiro número: '))

resultado = calculadora(num1, num2, op)
print(f'O resultado da operação é: {resultado}')

