# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.


def voto(ano_nasc):
    # importar dentro da função enocomiza memória
    from datetime import date
    ano_atual = date.today().year

    idade = ano_atual - ano_nasc
    if idade < 17:
        return f"Com {idade} tem o VOTO NEGADO"
        #print(f"VOTO NEGADO: Com {idade} anos é considerado menor de idade")
    elif idade <= 64:
        return f"Com {idade} VOTO OBRIGATÓRIO"
        #print(f"VOTO OBRIGATÓRIO: Com {idade} anos o voto é obrigatório")
    else:
        return f"Com {idade} VOTO OPCIONAL"
        #print(f"VOTO OPCIONAL: Com {idade} anos o voto é opcional")


print("-"*30)
nas = int(input("Em que ano você nasceu? "))
print(voto(nas))