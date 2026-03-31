# Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra "A". Em que posição ela aparece a primeira vez. Em que posição ela aparece a última vez.

frase = str(input('Digite uma frase: ')).lower()
count = frase.count('a')
primeiro_find = frase.find('a')
ultimo_find = frase.rfind('a')
print('A frase tem um total de {} letras a  '.format(count))
print('A primeira letra (a) está localizada no índice {}'.format(primeiro_find+1))
print('O ultima letra (a) está localizada no índice {}'.format(ultimo_find+1))