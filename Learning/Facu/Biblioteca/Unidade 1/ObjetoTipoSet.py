meu_conjunto = set()

meu_conjunto.add(10)
meu_conjunto.add(20)
meu_conjunto.add(30)

elemento = 20
if elemento in meu_conjunto:
    print(f"{elemento} está no conjunto.")
else:
    print(f"{elemento} não está no conjunto")

meu_conjunto.remove(20)
meu_conjunto.add(40)

print(f"Conjunto após remover o elemento 20 e adionado o 40, o conjunto ficou {meu_conjunto}")