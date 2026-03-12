# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo

while True:
    n = int(input('Digite um número: '))
    print('-'*30)
    if n < 0:
        break
    else:
        for c in range (1, 11):
            m = c * n
            print(f"{n} x {c} = {m}") 
    print('-'*30)
print("Fim")
             

