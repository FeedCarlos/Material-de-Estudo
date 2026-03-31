# Crie um programa que leia um nome de uma cidade e diga se ele começa ou não com o nome "SANTO"

cidade = str(input('Digite sua cidade: ')).strip()

print(cidade[:5].upper() == 'SANTO')




#busca = cidade.find('Santo'[0])

#if busca == 0:
#    print('Sua cidade começa com Santo')
#else:
#    print('Sua cidade não começa com Santo')

