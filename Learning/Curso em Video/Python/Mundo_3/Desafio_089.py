# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

cadastro = []
temp = []
while True:
    name = str(input("Nome do Aluno: "))
    temp.append(name)
    note1 = float(input("1º nota: "))
    temp.append(note1)
    note2 = float(input("2º nota: "))
    media = (note1 + note2) / 2
    temp.append(note2)
    temp.append(media)
    cadastro.append(temp[:])
    temp.clear()
    ask = str(input("Gostaria de adicionar mais? [S/N] "))
    print()
    if ask in 'Nn':
        break
print('-='*20)
print(f"{'No. NOME':<15} MÉDIA")
print('--'*20)
for c, l in enumerate(cadastro):
    print(f'{c}   {l[0]:<12} {l[3]}')
while True:
    print('--'*25)
    ask_note = int(input("Mostrar notas de qual aluno? [999] para sair: "))
    if ask_note != 999:
        c = ask_note
        if ask_note >= 0 and ask_note < len(cadastro):
            print(f'Boletim de {cadastro[c][0]} foi:\n1ºNota: {cadastro[c][1]}\n2ºNota: {cadastro[c][2]}')
        else:    
            print("Buscar nota de aluno listado!")
    else:
        print('Saindo')
        break