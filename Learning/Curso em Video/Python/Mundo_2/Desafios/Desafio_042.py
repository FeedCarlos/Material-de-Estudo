# Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado: - Equilátero: todos os lados iguais - Isósceles: dois lados iguais - Escaleno: todos os lados diferentes

a = float(input('Digite um valor: '))
b = float(input('Digite outro valor: '))
c = float(input('Digite outro valor: '))


if a < b + c  and b < a + c and c < a + b:
    print('Os valores podem formar um triângulo ', end='')
    if a == b == c:
        print('Equilátero!')
    if a != b != c != a:
        print('Escaleno')
    else:
        print('Isóceles')

'''
if cond1 == cond2 and cond1 == cond3 and cond2 == cond3:
    print('Os valores a-{}, b-{}, c-{} forma um Triângulo Equilátero.')
elif cond1 == cond2 or cond1 == cond3 or cond2 == cond3:
    print('Os valores a-{}, b-{}, c-{} forma um Triângulo Isósceles')
elif cond1 != cond2 and cond1 != cond3 and cond2 != cond3:
    print('Os valores a-{}, b-{}, c-{} forma um Triângulo Escaleno')
else: 
    print('Esses valores não formam um triângulo')'''
    