mulheres = ['Ana', 'Paula', 'Fernanda']


if len(mulheres) == 1:
    print(f"Só houve uma única mulher cadastrada, que foi a {' '.join(mulheres)}")
elif len(mulheres) > 1:
    print(f"As mulheres cadastradas foram {', '.join(mulheres[:-1])} e {mulheres[-1]}")
else:
    print("Não houve mulheres cadastradas!")