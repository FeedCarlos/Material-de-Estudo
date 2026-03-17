# Fala um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
import random
from time import sleep

print('-'*30)
print('''Vamos jogar Ímpar ou Par!''')
print('-'*30)
sleep(1)

r_e = ''
result = ''
count = 0
win = ''
inteiro = 0

while True:
    n_r = random.randrange(1,10)

    while True:
        e = str(input('Você quer ímpar ou par? [I | P]: '))
        if e not in 'PpIi':
            break

        n = int(input('Digite um número: '))

        if e == 'p':
            e = 'par'
            r_e = 'ímpar'
        else:
            r_e = 'par'
            e = 'ímpar'

        s = n_r + n 
        inteiro = s % 2

        if inteiro == 0:
            result = 'par'
        else:
            result = 'ímpar'
        
        if e == result:
            win = 'Venceu!'
            count += 1
            print('-'*30)
            print(f'Eu escolhi {n_r} e você {n}\nO total foi {s}\nSua escolha foi {e}\nEu escolhi {r_e}\nVocê {win}')
            print('-'*30)
        else:
            win = 'Perdeu!'
            print('-'*30)
            print(f'Eu escolhi {n_r} e você {n}\nO total foi {s}\nSua escolha foi {e}\nMinha escolha foi {r_e}\nFim de jogo!\nVocê teve {count} vitórias')
            print('-'*30)
            break
    r = str(input('Gostaria de jogar novamente? [S/N]')).upper()
    if r == 'S':
        print('-'*30)
        print('Reiniciando')
        print('-'*30)
        count = 0
        sleep(1)
    else:
        break
print('FIM')