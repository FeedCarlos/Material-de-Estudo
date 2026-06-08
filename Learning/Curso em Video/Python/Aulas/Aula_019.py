# Dicionário 
'''
dados = list()
dados.append('Pedro')
dados.append(25)
print(dados[0])
print(dados[1])


#dados = dict()
#dados = {}

dados = {'nome':'Pedro','idade':25}
dados['sexo'] = 'M'
del dados['idade']
print(dados['nome'])
#print(dados['idade'])
print(dados['sexo'])


filme = {
    'titulo':'Star Wars',
    'ano':1977,
    'diretor':'Geaoge Lucas'
}

#print(filme.values())
#print(filme.keys())
#print(filme.items())

for k, v in filme.items():
    print(f'O {k} é {v}')


pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}

print(f'O {pessoas ["nome"]} tem {pessoas["idade"]} anos')
#del pessoas['sexo']
pessoas['nome'] = 'Leandro'
pessoas['peso'] = 98.5
for k, v in pessoas.items():
    print(f'{k} = {v}')

brasil = []
estado = {'uf': 'Rio de Janeiro', 'sigla':'RJ'}
estado2 = {'uf':'São Paulo', 'sigla':'SP'}
brasil.append(estado)
brasil.append(estado2)

print(brasil[1]['sigla'])
'''

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()
