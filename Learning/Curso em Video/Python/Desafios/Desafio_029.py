# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi ultado. A multa vai custar 7,00 por cada Km acima do limite. 

velo = int(input('Qual é a velocidade do carro? '))
velo_max = 80
velo_calc = velo - velo_max
if velo > velo_max:
    print('Você está {}Km acima da velocidade permitida, o valor da multa é R$ {:.2f}'.format (velo_calc, velo_calc * 7))
else:
    print('Você está velocidade permitida')

