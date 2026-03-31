# Escreva um programa para aprovar o empréstimo bancário para a compra vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#Calcule o valor da prestação mensal, sabendo que ele não pode execer 30% do salário ou então o empréstimo será negado.
print('-'*40)
valor_casa = float(input('Qual é o valor da casa? '))
print('-'*40)
salario = float(input('Digite seu salário: '))
print('-'*40)
anos = int(input('Quantos anos você pretende pagar? '))
print('-'*40)
porcetagem = salario * 30 / 100

emprestimo = ((valor_casa) / (anos * 12))

if emprestimo <= porcetagem:
    print('\033[1;32mParabéns você foi APROVADO!\nSuas parcelas ficou R${:.2f}\nEsse valor vai ser pago em {} meses.\033[m'.format(emprestimo, (anos*12)))
elif emprestimo >= porcetagem:
    print('\033[1;31mInfelizmente você foi RECUSADO\nAs parcelas ficaram R${:.2f}\nExcedendo o 30% do seu salário.\033[m'.format(emprestimo))
else:
    print('Não pode ser calculado com valor zero!')