# Desenvolva um programa que pergunte a dustância de uma viagem em Km. Calcule o preço da passagem, cobrando 0,50 por Km para viagens de até 200Km e 0,45 para viagens mais longas.

distancia = int(input('A viagem tem quantos Km? '))

preco_1 = distancia * 0.50

preco_2 = distancia * 0.45

if distancia < 200:
    print('A viagem de {}Km vai custar R$ {:.2f}'.format(distancia, preco_1))
else:
    print('A viagem de {}Km vai custar R$ {:.2f}'.format(distancia, preco_2))