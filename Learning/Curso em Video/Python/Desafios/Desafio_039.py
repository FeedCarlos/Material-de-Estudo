# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade: -Se ele ainda vai se alistar ao serviço militar. -Se é a hora de se alistar. -Se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

year = date.today().year

nascimento = int(input('Digite sua data de nascimento: '))

if (year-nascimento) > 18:
    print('O tempo de alistamento já passou, foi a {} anos.'.format((year-nascimento)-18))
elif (year-nascimento) < 18:
    print('Ainda falta um tempo para o alistamento, {} anos'.format((nascimento+18)-year))
elif (year-nascimento) == 18:
    print('Está na época do alistamento!!')
elif nascimento > year:
    print('Data incorreta, por favor inserir data novamente.')