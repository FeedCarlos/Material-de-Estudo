# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo e realize a contagem.
'''
Seu programa tem que realizar três contagens através da função criada:

a) De 1 até 10, de 1 em 1
b) De 10 até 0, de 2 em 2
c) Uma contagem personalizada.
'''

from time import sleep


def contador(i, f, p):
    print("=-"*20)
    print(f"Contagem de {i} até {f} de {p} em {p}.")

    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    
    if i < f:
        ini = i
        while ini <= f:
            sleep(0.5)
            print(f"{ini} ", end='')
            ini += p
        print('FIM')
    else:
        ini = i
        while ini >= f:
            sleep(0.5)
            print(f'{ini} ', end='')
            ini -= p
        print("FIM")
        

contador(1, 10, 1)
contador(10, 0, 2)
print("=-"*20)
print("Agora é sua vez de personalizar a contagem")
ini = int(input('Ínicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(ini, fim, passo)

