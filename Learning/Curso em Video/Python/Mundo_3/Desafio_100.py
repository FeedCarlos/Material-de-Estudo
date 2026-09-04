# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeria função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

from time import sleep
from random import randint

numeros = []

def sorteia():
    for _ in range(0, 5):
        num = randint(0, 10)
        numeros.append(num)
    sleep(0.5)
    print(f"Sorteando 5 valores: ", end='')
    for v in numeros:
        sleep(0.5)
        print(f"{v} ", end='')

def somaPar():
    s = 0
    for v in numeros:
        if v % 2 == 0:
            s += v
    sleep(0.5)
    print(f"\nSomando todos os valores par da lista {numeros} vai dar {s}")


sorteia()
somaPar()
#print(numeros)
