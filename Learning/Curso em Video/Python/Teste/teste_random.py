# Importando uma biblioteca aleatória
import random
# Criando uma variável que vai sortiar um número entre 1 e 3, utilizando (randint) para número inteiro 
num = random.randint(1, 3)
ad = int(input('Adivinhe um número de 1 a 3: '))
if num == ad :
    print('Parabéns o número sortiado era {}, seu system32 não será deletado'.format(num))
else:
    print('Que pena o número sortiado era {}, seu system32 será molestado :) '.format(num))
