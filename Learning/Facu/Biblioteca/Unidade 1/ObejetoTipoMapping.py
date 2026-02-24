# Criação de um dicionário vazio, seguido de atribuição de chaves e valores
dici_1 = {}
dici_1 ['nome'] = "Maria"
dici_1 ['idade'] = 25

print(dici_1)

# Criação de um dicionário com pares chave: valor
dici_2 = {'nome': 'Maria', 'idade': 25}
# Criação de um dicionário com uma lita de tuplas representando pares chave : valor
dici_3 = dict([('nome', 'Maria' ('idade', 25))])
# Criação de um dicinário usando a função built-it zip() e duas listas, uma para as chaves e outra para os valores
dici_4 = dict(zip(['nome', 'idade'], ["Maria", 25]))
# Teste se todas as construções resultam em objetos iguais
print(dici_1 == dici_2 == dici_3 == dici_4) # Deve imprimir true
print(dici_1)