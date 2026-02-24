# Estrutura de repetição

# Laços de Repetição

"""
laço c no intervalo(1,10):
    passo
    pega

for c in range(1,10):
    passo
    pega

laço c no intervalo(0,3):
    passo
    pula
passo
pega


for c in range(0,3):
    passo
    pula
passo
pega


laço c no intervalo(0,3):
    se tiver coin
        pega
    passo
    pula
passo
pega

for c in range(0,3):
    if coin:
        pega
    passo
    pula
passo
pula
"""
'''
for c in range(0,10):
    print('Hello')
print('Fim')
'''
for c in range(10,0, -1):
    print(c)
print("Fim")
'''
for c in range(0,7,1):
    print(c)
print("Fim")'''

#n = int(input('Digite um número: '))
#for c in range(0, n+1):
#    print(c)
#print('FIM')

#i = int(input('Início: '))
#f = int(input('Fim: '))
#p = int(input('Passo: '))
#for c in range(i, f+1, p):
#    print(c)
#print('FIM')

#for c in range(0, 4):
#    n = int(input('Digite um valor: '))
#print('FIM')

#s = 0
#for c in range(0,5):
#    n = int(input("Digite um número: "))
#    s += n
#print('O somatório dos numéros foi {}'.format(s))