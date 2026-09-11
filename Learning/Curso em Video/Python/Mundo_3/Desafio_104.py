# Crie um programa que tenha a função leiaInt() que vai funcionar de forma semelhante à função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico. 
# EX: n = leiaInt('Digite um n')

def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            ok = True
            valor = n
        else:
            print("\033[0;31mERRO! Digite um valor válido.\033[m")
        if ok == True:
            break
    return valor

n = leiaInt("Digite um número: ")
print(f"O número digitado foi {n}")   
#n = leiaInt("Digite um número: ")