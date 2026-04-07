# Crie uma tupla preenchida com os 20 primeiros colocados da tabela do campeonato brasileiro de futebol, na ordem de colocação. Depois mostre:
# A) Apenas os 5 primeiros colocados. - B) Os últimos 4 colocados da tabela - C) Uma lista com os times em ordem alfabética. - D) Em que posição na tabela está o time da Chapecoense

brasileirao = ('Palmeiras', 'Athletico PR', 'São Paulo', 'Fluminense', 'Flamengo', 'Bahia', 'Coritiba', 'Grêmio', 'Vasco da Gama', 'Vitória', 'Corinthians', 'Internacional', 'Atlético-MG', 'Red Bull Bragantino', 'Chapecoense', 'Santos', 'Botafogo', 'Mirassol', 'Remo-PA', 'Cruzeiro')
print('-'*30)
print('   TABELA DO BRASILEIRÃO')
print('-'*30)
print('   OS Primeiros 5 Colocados\n')
print(f'''1º {brasileirao[0]}
2º {brasileirao[1]}
3º {brasileirao[2]}
4º {brasileirao[3]}
5º {brasileirao[4]}\n''')
print('')
print('-'*30)
print('Os Últimos 4 Colocados')
print('-'*30)
print('')
print(f'''10º {brasileirao[-1]}
9º {brasileirao[-2]}
8º {brasileirao[-3]}
7º {brasileirao[-4]}\n''')
print('-'*30)
print('   Em Ordem Alfabética')
print('-'*30)
print('')
print(sorted(brasileirao))
print('')
print('-'*30)
print('   A Posição do Chapecoense')
print('-'*30)
print('')
chapecoense = brasileirao.index('Chapecoense')
chapecoense += 1
print(f'{chapecoense}º Chapecoense')
print('')