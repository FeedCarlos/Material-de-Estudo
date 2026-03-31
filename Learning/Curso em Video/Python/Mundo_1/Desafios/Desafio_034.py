# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários supriores a 1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Qual é seu salário? R$'))

if salario > 1250:
    print('O seu salário de {:.2f} vai receber um aumento de 10%, ficando {:.2f} '.format(salario, ((salario*10)/100)+salario ))
elif salario <= 1250:
    print('O seu salário de {:.2f} vai receber um aumento de 15%, ficando {:.2f}'.format(salario, ((salario*15)/100)+salario))