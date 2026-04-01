# Importando a biblioteca Math
# from (da) biblioteca Math quero importar só sqrt
from math import sqrt,ceil

num = int(input('Digite um número: '))
# Utilizando math.sqrt para encontar a raiz de um número
raiz = sqrt(num)
# Printando o valor e utilizando math.ceil para arrendondar para cima ou math.floor para arrendondar para baixo
print('A raiz de {} é igual a {:.2f}'.format(num, ceil(raiz)))