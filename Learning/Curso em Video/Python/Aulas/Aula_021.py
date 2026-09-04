# Interactive Help
'''
Utilizar a função help()
'''
#print(input.__doc__)
#help(input)

# DOCSTRINGS
# def contador(i, f, p):
#     """
#     Faz uma contagem e mostra na tela
#     :param i: início da contagem
#     :param f: fim da contagem
#     :param p: passo da contagem
#     :return: sem retorno
#     Função criado por Gustavo Guanabara
#     """
#     c = i
# 
# help(contador)

# Parâmetro Opcional

# def somar(a, b, c=0):
#     s = a + b + c
#     print(f"A soma vale {s}")
# 
# 
# somar(3, 2, 5)
# somar(8, 4)

# Escopo de Variáveis
# def teste():
#     global n1
#     print(f"N1 dentro vale {n1}")
# 
# 
# # Programa principal
# n1 = 2
# print(f"N1 fora vale {n1}")
# teste()

# Return

# def somar (a=0, b=0, c=0):
#     s = a + b + c
#     return s
#     #print(f"A soma vale {s}")
# 
# #print(somar(3, 2, 5))
# r1 = somar(3, 2, 5)
# r2 = somar(1, 7)
# r3 = somar(6)
# 
# print(f"Os resultados foram {r1}, {r2}e {r3}")

# def fatorial(num = 1):
#     f = 1
#     for c in range(num, 0, -1):
#         f *= c
#     return f

# n = int(input("Digite um número: "))
# print(f'O fatorial de {n} é igual a {fatorial(n)}')

# f1 = fatorial(5)
# f2 = fatorial(4)
# f3 = fatorial()
# print(f'Os resultados de {f1}, {f2} e {f3}')

def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input("Digite um número: "))
if par(num) == True:
    print("É par")
else:
    print("É ímpar")