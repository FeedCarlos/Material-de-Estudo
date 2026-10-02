def aumentar(num):
    v = num + ((num / 100) * 10)
    return v


def diminuir(num):
    v = num - ((num / 100) * 10)
    return v


def dobro(num):
    v = num * 2
    return v


def metade(num):
    v = num / 2
    return v


def moeda(num):
    m = (f"R$ {num:.2f}")
    return m