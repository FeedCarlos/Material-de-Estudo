valor_produto = float(input('Qual o valor do produto? '))

desconto = (5 / 100) * valor_produto

total = valor_produto - desconto

print('Valor do produto é {} com o desconto de 5% fica {:.2f}'. format(valor_produto, total))