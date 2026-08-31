# Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
def Controle():
    print(" Controle de Terrenos ")
    print("-"*25)

def calculo():
    calc = largura * comprimento
    print(f"A área de um terreno {largura}x{comprimento} é de {calc}m².")

Controle()
largura = float(input("LARGURA (m): "))
comprimento = float(input("COMPRIMENTO (m): "))
calculo()