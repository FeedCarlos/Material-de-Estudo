# Faça um programa que leia um número de 0 a 9999 e monstre na tela cada um dos dígitos separados.
# Ex: Digite um número: 1834 - unidade 4 - dezena 3 - centena 8 - milhar 1

num = int(input('Digite um número entre 0 e 9999: '))

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print('Analisando o número {}'.format(num))
print('Unidade {}'.format(u))
print('Dezena {}'.format(d))
print('Centena {}'.format(c))
print('Milhar {}'.format(m))

#Unidade = (num[0])
#Dezena = (num[1])
#Centena = (num[2])
#Milhar = (num[3])


#print('O número é {}\nUnidade {}\nDezena {}\nCentena {}\nMilhar {}'.format(num, num[0], num[1], num[2], num[3]))
#print('O número é {}\nUnidade {}\nDezena {}\nCentena {}\nMilhar {}'.format(num, Unidade, Dezena, Centena, Milhar))
