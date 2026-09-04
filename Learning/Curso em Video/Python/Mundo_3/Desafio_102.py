# Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e o outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

print("~"*12)
print(" Fatorando ")
print("~"*12)
print()

def fatorial(num = 1, show=True):
    f = 1
   
    for v in range(num, 0, -1):
        f *= v
        if show:
            if v > 1:
                print(f"{v} x ", end='')
            else:
                print(f"{v} = ", end='')
    return f


print(f"{fatorial(4)}")




