cadastro = [["Carlos", 10, 8], ["Ana", 5, 7]]
print(len(cadastro))
ask = int(input('Gostaria de ver a nota de quem? '))
for c, j in enumerate(cadastro):
    if c == ask:
        print(cadastro[c][0])