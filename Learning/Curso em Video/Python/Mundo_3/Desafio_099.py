# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
print("=-"*25)
print("Vamos Análisar e Descobrir o Maior Numero")
print("=-"*25)

def maior(*nums):
    print("Análisando os valores passados:")
    if nums == '':
        print("O único valor passado foi 0")
    else:        
        for v in nums:
            print(f"{v} ", end='')
        maior = max(nums)
        print(f"\nTotal de {len(nums)} números.")
        print(f"O maior número análisado foi {maior}")
        print("-"*30)

maior(5, 2, 4, 7, 9, 2, 1)
maior(5, 2, 4, 7)
maior(9, 2, 1)
maior(5)
#maior()

