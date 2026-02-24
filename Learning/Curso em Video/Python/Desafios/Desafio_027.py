# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
# Ex: Ana Maria de Souza - Primeiro: Ana. Último: Souza

nome = str(input('Digite seu nome: ')).strip()

first_name = nome.split()

print('Seu primeiro nome é {}'.format(first_name[0]))
print('Seu último nome é {}'.format(first_name[len(first_name)-1]))

