valor_produto = float(input("Digite o valor do produto: "))
desconto = float(input("Digite o porcentual de desconto: "))

if desconto < 0 or desconto > 100:
    print("Erro: O porcentual de desconto deve estar entre 0% e 100%")
else:
    desconto = valor_produto * (desconto / 100)

valor_final = valor_produto - desconto

print(f"Valor com desconto : R$ {valor_final:.2f}")