# Refaça o desafio 009, monstrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
n = int(input('Digite o número que gostaria de ver a tabuada: '))
for c in range(1, 11):
    print(f'{n} x {c} = {n*c}')
print('FIM')
    