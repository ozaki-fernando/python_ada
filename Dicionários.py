# DICIONÁRIOS

#Criando dicionários

dicionario = {}
dicionario = dict()

dicionario = { 'nome': 'Fernando', 'idade': 31, 'altura': 1.71 }

print (dicionario)
print (dicionario['nome'])

# Adicionando elementos no dicionario
dicionario['programador']=True
print(dicionario)
dicionario['altura'] = 2
print(dicionario)

# Iterando sobre um dicinário

for chave in dicionario:
    print(chave, dicionario[chave])

# Testando a existencia de uma chave
print('peso' in dicionario)
print('altura' in dicionario)