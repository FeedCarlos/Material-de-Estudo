# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles. (desconsiderando o flag)

n = int(input('Digite alguns números para vermos a soma ou digite 999 para sair\nDigite ou [999 para sair]: '))
count = 0
total = 0
if n != 999:
    while n != 999:
        if n > 999:
            print('Não ultrapasse o limite')
        else:
            soma = n + total
            total = soma
        n = int(input('Digite outro [999 para sair]: '))
        count += 1
    print('-='*40)
    print('Soma total é {} e foram digitados {} números'.format(total, count))
print('-='*40)
print('FIM!')