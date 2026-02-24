#vogais = ('a', 'e', 'i', 'o', 'u')
#print(f'Tipo de objeto vogais = {type(vogais)}')
#for p, x in enumerate(vogais):
#    print(f'Posição = {p}, valor = {x}')

# Tupla de convidados
convidados = ('Alice', "Bob", "Carol", "David", "Eve")
# Lista de confirmações 
confirmados = ["Bob", "David"]

# Identificar quem ainda não confirmou
nao_confirmados = [convidado for convidado in convidados if convidado not in confirmados]
# Exibir os convidados que ainda não confirmaram
print("Convidados que ainda não confirmaram: ")
for pessoa in nao_confirmados:
    print(pessoa)
# Enviar lembretes aos não confirmados
print("\nEnviando lembretes para os convidados que ainda não confirmaram")