# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.
import moeda

valor = float(input("Digite uma valor: "))
aumento =  moeda.aumentar(valor)
desconto = moeda.diminuir(valor)
dobro = moeda.dobro(valor)
metade = moeda.metade(valor)

print(f"Um aumento de 10% em {valor:.2f} é {aumento:.2f}") 
print()
print(f"Um desconto de 10% em {valor:.2f} é {desconto:.2f}")
print()
print(f"O dobro de {valor:.2f} é {dobro:.2f}")
print()
print(f"A medade de {valor:.2f} é {metade:.2f}")
