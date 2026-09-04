# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.
from datetime import date

ano_atual = date.today().year

def voto(ano_nasc):
    idade = ano_atual - ano_nasc
    if idade < 17:
        return "VOTO NEGADO"
        #print(f"VOTO NEGADO: Com {idade} anos é considerado menor de idade")
    elif idade <= 64:
        return "VOTO OBRIGATÓRIO"
        #print(f"VOTO OBRIGATÓRIO: Com {idade} anos o voto é obrigatório")
    else:
        return "VOTO OPCIONAL"
        #print(f"VOTO OPCIONAL: Com {idade} anos o voto é opcional")


print(voto(1889))     