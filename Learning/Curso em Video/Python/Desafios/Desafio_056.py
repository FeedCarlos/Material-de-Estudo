# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, monstre:
# A média de idade do grupo.
# Qual é o nome do homem mais velho.
# Quantas mulheres têm menos de 20 anos.

sexo_f = 0
total_idade = 0
m_velho = ''
m_velho_idade = 0

for p in range(1, 5):
    print('---- {}ª PESSOA ----'.format(p))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: '))
    total_idade += idade  
    if p == 1 and sexo in 'Mm':
        m_velho_idade = idade
        m_velho = nome
    if sexo in 'Mm' and idade > m_velho_idade:
        m_velho = nome
        m_velho_idade = idade
    if idade < 20 and sexo in 'fF':
        sexo_f += 1
        
        
media = total_idade / 4

print('A média de idade do grupo é {}'.format(media))
print('O nome do homem mais velho é {} e tem {}'.format(m_velho, m_velho_idade))
print('No grupo tem {} mulheres com menos de 20 anos.'.format(sexo_f))