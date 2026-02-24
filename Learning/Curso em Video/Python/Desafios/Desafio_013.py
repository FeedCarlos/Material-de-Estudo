salario = float(input('Qual é o seu salário? '))

porcen_aumento = (15 / 100) * salario

novo_salario = salario + porcen_aumento

print('O seu salário teve um aumento de 15% o valor adicional ficou {:.2f}, seu novo salário é {}'.format(porcen_aumento, novo_salario))