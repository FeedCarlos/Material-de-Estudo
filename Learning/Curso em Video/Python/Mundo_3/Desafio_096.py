# Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

def area(largura, comprimento):
    resultado = largura * comprimento
    print(f"A área de um terreno {largura}x{comprimento} é de {resultado}m².")

print(" Controle de Terreno ")
print("-"*25)
largura = float(input("Largura (m): "))
comprimento = float(input("Comprimento (m): "))
area(largura, comprimento)

