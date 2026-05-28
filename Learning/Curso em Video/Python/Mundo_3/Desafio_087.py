# Aprimore o desafio anterior, mostrando no final: A) A soma de todos os valores pares digitados. B) A soma dos valores da terceira coluna C) O maior valor da segunda linha 

matrix = [[0,0,0], [0,0,0], [0,0,0]]
count = 1
soma = s_par = s_terColum = m_valorSegunL = 0

for linha in range(0, 3):
    for coluna in range(0, 3):
        matrix[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]'))
print('-='*30)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matrix[linha][coluna]:^5}]', end='')
        if matrix[linha][coluna] % 2 == 0:
            s_par = matrix[linha][coluna] + s_par
        #soma = matrix[linha][coluna] + soma
    print()

print('-='*30)
#print(f'O resultado da soma dos números é {soma}')
print(f'O resultado da soma dos números par é {s_par}')
for linha in range(0, 3):
    s_terColum += matrix[linha][2]
print(f'A soma dos valores da terceira coluna é {s_terColum}')
for c in range(0, 3):
    if c == 0:
        m_valorSegunL = matrix[1][c]
    elif matrix[1][c] > m_valorSegunL:
        m_valorSegunL = matrix[1][c]        
print(f'O maior valor da segunda linha é {m_valorSegunL}')
