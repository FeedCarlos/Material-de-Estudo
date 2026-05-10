# Variáveis Compostas (Listas)

'''
dados = list()
dados.append('Pedro')
dados.append(25)

#pessoas = list()
#pessoas.append(dados[:])

pessoas = [["Pedro",25], ['Maria', 19]]

print(pessoas[1][1])


teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 18
galera.append(teste[:])
print(galera)

galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade. ')
'''

galera = list()
dado = list()
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

print(f'{galera}')
'''
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maoir de idade.')
    else:
        print(f'{p[0]} é menor de idade.')
'''