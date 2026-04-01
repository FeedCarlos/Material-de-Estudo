# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extensão, de zero até 20.
# Seu programa de verá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso

contagem = ('um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if num > 20 or num < 0:
        print('Erro: Digite um número válido entre 0 e 20: ')
    else:
        break
print(f'Você digitou o número {contagem[num - 1]}')