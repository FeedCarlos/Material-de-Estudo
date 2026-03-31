# Crie um programa que leia o nome completo da pessoa e mostre. - O nome com todas as letras maiúsculas. - O nome com todas minúsculas. - Quantas letras ao todo (sem considerar espaços). - Quantas letras tem o primeiro nome.

nome = input(str('Digite seu nome: '))
nome_sem_espaço = nome.replace(' ', '')
nome_cortado = nome.split()
print('O nome é {}'.format(nome))
print(nome.upper())
print(nome.lower())
print(len(nome_sem_espaço))
#print(len(nome_cortado[0]))
print('Seu primeiro nome é {}, contém {} letras'.format(nome_cortado[0], len(nome_cortado[0])))