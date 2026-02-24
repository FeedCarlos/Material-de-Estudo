# Estrutura condicional 

# se carro.esquerda()
    # bloco_v_
# senão
    # bloco_f_

# Condição

#if carro.esquerda():
#    bloco True
#else:
#    bloco False

tempo = int(input('Quantos anos tem seu carro? '))
if tempo <= 3:
    print('Carro novo')
else:
    print('Carro velho')
print('--FIM--')

# Condição Simplificada

tempo = int(input('Quantos anos tem seu carro? '))
print('Carro novo' if tempo <=3 else 'Carro velho')
print('--FIM--')