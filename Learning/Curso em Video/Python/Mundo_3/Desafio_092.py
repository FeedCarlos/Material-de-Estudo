# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário se por acaso o CTPS for diferente de ZERO, também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aponsentar.

# Quais infomações o usuário deve digitar: 
# nome - ano de nascimento - carteira de trabalho - ano de contratação - salário

# Quais informções o programa vai calcular:
# ano de nascimento - quanto tempo para se aposentar

# Qual será a estrutura final do dicionário: 
# -nome
# -idade
# -CTPS
# -ano_contra
# -salário
# -ano_p_aposent

# Em que momento será utilizado o IF:
# IF CTPS != de 0

from datetime import datetime

ano_atual = datetime.now().year

cliente = {}

ANO_CONTRIBUICAO = 35

cliente["nome"] = input("Digite seu nome: ").title()
cliente["ano_nasc"] = int(input("Digite seu ano de nascimento: "))
cliente["idade"] = ano_atual - cliente["ano_nasc"]
cliente["CTPS"] = int(input("Digite o número da sua carteira de trabalho (digite 0 caso não tenha): "))

if cliente["CTPS"] != 0:
    cliente["ano_contra"] = int(input("Digite o ano de contratação: "))
    while cliente["ano_contra"] > ano_atual:
            cliente["ano_contra"] = int(input("Digite um ano válido!: "))
    cliente["salário"] = float(input("Digite seu salário: "))
    cliente["ano_p_aposen"] = cliente["idade"] + (ANO_CONTRIBUICAO - (ano_atual - cliente["ano_contra"]))

print()
print('-='*30) 

if cliente["CTPS"] != 0:
    print(f'''
{cliente["nome"]} nascido em {cliente["ano_nasc"]} tem {cliente["idade"]} anos.
Seu número da carteira de trabalho é {cliente["CTPS"]}, o ano da contratação foi em {cliente["ano_contra"]}.
O salário recebido é {cliente["salário"]:.3f}.
Aposentadoria prevista com {cliente["ano_p_aposen"]} anos.
''')
else:
    print(f'''
{cliente["nome"]} nascido em {cliente["ano_nasc"]} tem {cliente["idade"]} anos.
Não possui número da carteira de trabalho, nem salário.
São necessários {ANO_CONTRIBUICAO} anos de contribuição para se aposentar.
''')
