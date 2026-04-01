# AS TUPLAS SÃO IMUTÁVEIS

# Variáveis Compostas (Tuplas)


'''
váriavel
lanche = hámburguer
lanche = suco PdLK02@

(tupla)
lache = hámburguer, suco, pizza, pudim
            0        1      2      3

print(lanche [2]) == pizza

print(lanche [0:2]) == hámburguer, suco

print(lanche [-1]) == pudim

len(lanche) = 4

for c in lanche:
    print(c)

            
'''

#lanche = ('Hámbuerguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')

'''# Tuplas são imutáveis | lanche[1] = 'Refirgerante'
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi muita coisa')'''

'''
for comida in lanche:
    print(f'Eu comi {comida}')
print('Comi pra caramba!')
'''

'''
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
'''
'''
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
print('Comi pra caramba!')

#print(len(lanche))
'''

# organiza a tupla = print(sorted(lanche))
'''
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
# Buscando quantos número 5
print(c.count(5))
# Procurando a posição do número
print(c.index(4))
'''

pessoa = ('Gustavo', 39, 'M', 99.88)
del pessoa
print(pessoa)