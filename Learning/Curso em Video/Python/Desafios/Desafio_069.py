# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A - quantas pessoa tem mais de 18 anos.
# B - quantos homens foram cadastrados.
# C - Quantas mulheres tem menos de 20 anos

more_18 = 0
man = 0
w_less_20 = 0
total = 0

print('='*30)
print('Vamos fazer o cadastro')
print('='*30)

while True:
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Qual é seu sexo [M/F]? '))
    while sexo not in 'MmFf':
        sexo = str(input('Digite um sexo válido! [M/F]: '))
    if idade >= 18:
        more_18 += 1
    if sexo == 'm':
        man += 1
    if idade < 20 and sexo =='f':
        w_less_20 += 1
    total += 1
    print('Cadastro realizado!')
    cont = str(input('Gostaria de continuar [S/N]? '))
    if cont not in 'Nn':
        print('-'*30)
        print('Reiniciando')
        print('-'*30)
    else:    
        break
print('Finalizadno')
print('='*40)
print(f'O total de cadastros foi {total}\nTotal de pessoas de maiores foi {more_18}\nO total de homens cadastrados foi {man}\nO total de mulheres menos de 20 anos foi {w_less_20}')
print('='*40)