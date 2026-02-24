# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tebela abaixo: - Aabaixo de 18.5: Abaixo do Peso - Entre 18.5 e 25: Peso ideal - 25 até 30: Sobrepeso - 30 até 40: Obesidade - Acima de 40: Obesidade mórbida

from time import sleep

print('Vamos calcular seu IMC', end='')
sleep(1)
print('.',end='')
sleep(1)
print('.',end='')
sleep(1)
print('.')

print('-'*30)
peso = float(input('Insira seu peso:  '))
print('-'*30)
print('Insira sua altura\nEx: 1.70')
altura = float(input('Agora insira sua altura: '))

imc = peso / (altura ** 2)

if imc < 18.5:
    print('Você está abaixo do peso! {:.1f}'.format(imc))
elif 18.5 <= imc < 25:
    print('Você está no peso ideal! {:.1f}'.format(imc))
elif 25 <= imc < 30:
    print('Você está com sobrepeso! {:.1f}'.format(imc))
elif 30 <= imc < 40:
    print('Você está na obesidade! {:.1f}'.format(imc))
else:
    print('Você está com obesidade mórbida! {:.1f}'.format(imc))
