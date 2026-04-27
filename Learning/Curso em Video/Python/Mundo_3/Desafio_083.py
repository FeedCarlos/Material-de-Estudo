# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na prdem correta.

expr = str(input('Digite a expressão: '))
pulha = []
for simb in expr:
    if simb == '(':
        pulha.append('(')
    elif simb == ')':
        if len(pulha) > 0:
            pulha.pop()
        else:
            pulha.append(')')
            break
if len(pulha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')