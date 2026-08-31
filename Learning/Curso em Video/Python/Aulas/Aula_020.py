'''
        Funções (tudo que pode ser repetitivo)

def mostreLinha():
    print('-----------------')

mostraLinha()
print('     Sistema de Alunos       ')
mostraLinha()
mostraLinha()
print('     Cadastro de Funcionários        ')
mostraLinha()
mostraLinha()
print('     Erro do Sistema     ')
mostraLinha()
'''
# def lin():
#     print('-'*30)

# # Programa Principal (Após a def deve ter duas linhas pela organização do código)
# lin()
# print('     Curso em Vídeo   ')
# lin()
# lin()
# print('     Aprenda Pyhton      ')
# lin()

'''
def mensagem(msg):
    print('-----------')
    print(msg)
    print('-----------')
mensagem('Sistema de Alunos')
'''
#def rotina(parâmetro)
# def título(txt):
#     print('-'*30)
#     print(txt)
#     print('-'*30)

# título('        Curso em vídeo      ')
# título('        Aprenda Python      ')
# título('        Carlos Daniel       ')

# a = 4
# b = 5
# s = a+b

# def soma(a, b):
#     print(f"A = {a} e B = {b}")
#     s = a + b
#     print(s)

# soma(a=4, b=5)
# # a = 8
# # b = 9
# # s = a+b
# soma(b=8, a=9)

# # a = 2
# # b = 1
# # s = a+b
# soma(2, 1)

'''
    Empacotar parâmetro


def contador(*núm):
    comtador(5, 7, 3, 1, 4)
'''

# def contador(*num):
#     tam = len(num)
#     for v in num:
#         print(f'Há {tam} números no primeiro contador = {v} ' if tam == len(num) end='')

# contador(2, 1, 7)
# contador(8, 0)
# contador(4, 4, 7, 6, 2)

# def dobra(lst):
#     pos = 0
#     while pos < len(lst):
#         lst[pos] *=2
#         pos += 1


# valores = [7, 2, 5, 0, 4]
# dobra(valores)
# print(valores)

def soma(*valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')

soma(3, 4, 5)
soma(2, 1)