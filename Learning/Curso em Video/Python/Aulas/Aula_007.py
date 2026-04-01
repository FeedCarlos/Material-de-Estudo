# Soma
ex1 = 5+3*2
ex2 = 5**2
ex3 = 5**3
ex4 = 19//2
ex5 = 19/2
ex6 = 365**522
ex7 = pow(4,2)
ex8 = '='*20

#print(ex8)

#nome = input("Qual é seu nome? ")
#print('Prazer em te conhecer {:=^20}!'. format(nome))

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
raiz = n1 ** 0.5
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
resto_divi = n1 % n2
print('A soma é {}, \n o produto é {} e a \n divisão é {:.3f}'.format(s,m,d), end=' >>> ')
print('Divisão inteira {}, potência {} e a raiz é {}'.format(di,e, raiz))