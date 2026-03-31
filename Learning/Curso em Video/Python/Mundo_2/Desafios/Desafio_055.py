# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e menor peso lidos.

maior_p = 0
menor_p = 0

for c in range(1,6):
    u = float(input(f'Peso da {c}ª pessoa: '))
    if c == 1:
        maior_p = u
        menor_p = u
    else:
        if u > maior_p:
            maior_p = u
        if u < menor_p:
            menor_p = u
print(f"O maior peso foi {maior_p} e o menor peso foi {menor_p}")

