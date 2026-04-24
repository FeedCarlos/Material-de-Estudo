# Aula 17 - Listas
# Variáveis Compostas (Listas)
'''
lanche = ['h', 's', 'piz', 'pu']
# Mudar um elemento
lanche[3] = 'pic'

# Adicionar um elemento
lanche.append('cok')

# Adicionar um elemento em uma posição específica
lanche.insert(0,'ca')

# Apagar um elemento
#del lanche[3]
# ou pop sem indicador ele remove o ultimo
#lanche.pop()
# Para eliminar pelo conteúdo
if 'pi' in lanche:
    lanche.remove('pi')
#lanche.remove('pi')
'''
'''
valores = list(range(4,11))
# Utilizando reverse=True para inverter a ordem
valores.sort(reverse=True)
# Utilizando len(valores)
print(len(valores))
print(valores)
'''
'''
num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 2)
if 4 in num:
    num.remove(4)
else:
    print('Não achei o número 4')
#num.pop(2)
print(num)
print(f'Essa lista tem {len(num)} elementos')
'''
'''
valores = []
for cont in range(0,5):
    valores.append(int(input('Digite um valor: ')))

'''
#valores.append(5)
#valores.append(4)
#valores.append(9)
'''
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Chequei todos os valores da lista')
'''

a = [2, 3, 4, 7]
b = a[:]
b[2] = 8

print(f'Lista A: {a}')
print(f'Lista B: {b}')