# Crie um programa que leia duas notas de um aluno e calcule sua mpedia, mostrando uma mensagem no final, de acordo com a média atingida: - Média abaixo de 5.0:Reprovado - Média entre 5.0 e 6.9:Recuperação: - Média 7.0 ou superior: Aprovado.

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2) / 2

if media < 5.0:
    print('\033[1;31mSua média foi {:.1f}. Reprovado\033[m'.format(media))
elif media == 5.0 or media < 6.9:
    print('\033[1;33mSua média foi {:.1f}. Está em recuperação\033[m'.format(media))
else:
    print('\033[1;32mSua média foi {:.1f}. Parabéns foi APROVADO!\033[m'.format(media))