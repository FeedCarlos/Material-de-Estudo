# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: A) Quantas pessoas foram cadastradas - B) A média de idade do grupo - C) Uma lista com todas as mulheres - D) Uma lista com todas as pessoas com idade acima da média.

# Informações que o usuário terá que inserir: 
# - nome - sexo - idade

# Informações que o programa terá que calcular/processar 
# - Quantidade de pessoas cadastradas - Média da idade - lista com todas as mulheres - lista com todas as pessoa acima da idade

# Estrutua do dicionário
# - nome 
# -     idade
# -     sexo
# - Quantidade de pessoas cadastradas
# - Média de idade do grupo
# - Uma lista [] com todas as mulheres
# - uma lista [] com todas as pessoas acima da média

registro = {}
cadastrados = []
mulheres = []
acima_media = []
soma_idade = 0

while True:
    registro['nome'] = input("Digite seu nome: ")
    registro['idade'] = int(input("Digite sua idade: "))
    while True:
        registro['sexo'] = input("Digite seu sexo[F/M]: ").capitalize()
        if registro['sexo'] not in "FM":
            print("Sexo inválido, por favor digite novamente!")
        else:
            break
    if registro['sexo'] == 'F':
        mulheres.append(registro['nome'])
    proximo = input("Gostaria de continuar[S/N]? ")
    cadastrados.append(registro.copy())
    if proximo in "Nn":
        break
for pessoas in cadastrados:
    soma_idade += pessoas['idade']
Qtde_Usuarios = len(cadastrados)
media = int(soma_idade/Qtde_Usuarios)
for idade_m in cadastrados:
    if idade_m['idade'] > media:
        acima_media.append(idade_m['nome'])

print()
print('-='*30)
print(f'''O total de pessoas cadastrados foram {Qtde_Usuarios}.
A média de idade do grupo foi de {media} anos.''')
if len(mulheres) == 1:
    print(f"Só houve uma única mulher cadastrada, que foi a {mulheres[0]}")
elif len(mulheres) > 1:
    print(f"As mulheres cadastradas foram {', '.join(mulheres[:-1])} e {mulheres[-1]}")
else:
    print("Não houve mulheres cadastradas!")
if len(acima_media) > 1:
    print(f"{', '.join(acima_media[:-1])} e {acima_media[-1]} estão acima da média")
elif len(acima_media) == 1:
    print(f"{''.join(acima_media)} está acima da média")
else:
    print("Não tem ninguém acima da média")
print('-='*30)
print()