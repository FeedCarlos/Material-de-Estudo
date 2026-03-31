# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
par = 0
for n in range(1, 7):
    num = int(input('Digite um valor: '))
    if num%2 == 0:
        par += num
print(f'O número total das somas foi {par}')
