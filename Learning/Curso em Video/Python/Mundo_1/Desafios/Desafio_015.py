days_car = int(input('Por quantos dias o carro foi alugado? '))
km = int(input('Quantos KM ele foi rodado? '))

total = (days_car*60) + (km*0.15)
#car = days_car*60
#km_ro = km * 0.15

print('O total a pagar é de R${:.2f}'.format(total))