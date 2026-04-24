# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, seráo exibidos todos os valores únicos digitados, em ordem crescente.

num = [int(input('Digite um número: '))]

while True:
    per = str(input("Gostaria de continuar? [S|N] "))
    
    if per in 'Ss':
        while True:
            try:
                o_num = int(input('Digite outro número: '))
                break
            except ValueError:
                print('ERRO! Digite um valor número inteiro!')
        if o_num not in num:
            print('Valor Cadastrado!')
            num.append(o_num)
        else:
            print('ERRO Item não Adicionado: Já existe esse valor na lista')
    else:    
        break
print('='*50)
num.sort()
print(f'Os números cadastrados foram {num}')
                
