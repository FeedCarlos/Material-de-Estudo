# A Confederação Nacional de Natação precisa de um programa que elia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade: - Até 9 anos: Mirim - Até 14 anos: Infantil - Até 19 anos: Junior - Até 20 anos: Sênior - Acima Master

from datetime import date

year_now = date.today().year

ano = int(input('Em qual ano você nasceu? '))

idade = year_now - ano

print (idade)

if idade <= 9:
    print('Com {} anos sua categoria é mirim.'.format(idade))
elif idade <= 14:
    print('Com {} anos sua categoria é infantil.'.format(idade))
elif idade <= 19:
    print('Com {} anos sua categoria é junior.'.format(idade))
elif idade <= 25:
    print('Com {} anos sua categoria é sênior.'.format(idade))
else:
    print('Com {} anos sua categoria é master'.format(idade))