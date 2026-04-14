# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre: A) Quantas vezes apareceu o valor 9. - B) Em que posição foi digitado o primeiro valor 3. - C) Quais foram os números pares.

num = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite outro número: ')))
print('-='*30)
print(f'Você digitou os seguintes números {num}')
nine = num.count(9)
if nine > 1:
    print(f'O número nove apareceu {nine} vezes')
elif nine == 1:
    print(f'O número nove apareceu {nine} vez')
else:
    print(f'O número nove não foi digitado')
if 3 in num:
    print(f'O valor 3 aparceu na {num.index(3)+1}ª posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print('Os valores pares digitados foram ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')