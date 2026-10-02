# Adapte o código do desafio 107, criando uma função adicional chamada moeda() que consiga mostrar os valores como um valor monetário formatado.

import moeda

valor = float(input("Digite uma valor: "))
print("-"*40)
aumento =  moeda.aumentar(valor)
desconto = moeda.diminuir(valor)
dobro = moeda.dobro(valor)
metade = moeda.metade(valor)

print(f"Um aumento de 10% em {moeda.moeda(valor)} é {moeda.moeda(aumento)}") 
print()
print(f"Um desconto de 10% em {moeda.moeda(valor)} é {moeda.moeda(desconto)}")
print()
print(f"O dobro de {moeda.moeda(valor)} é {moeda.moeda(dobro)}")
print()
print(f"A medade de {moeda.moeda(valor)} é {moeda.moeda(metade)}")