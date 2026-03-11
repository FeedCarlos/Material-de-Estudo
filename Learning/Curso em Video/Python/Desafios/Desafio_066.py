# Crie um programa que leia vários númeors inteiros pelo teclado. O progamara só vai para quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles. ( Desconsiderando o flag).

n = count = s = 0
while n != 999:
    n = int(input("Digite um número [999 para sair]: "))
    if n == 999:
        break
    count += 1
    s = n+n
print('-'*40)
print(f'Quantidade de números digitados {count}\nSoma entre eles {s}')
print('-'*40)