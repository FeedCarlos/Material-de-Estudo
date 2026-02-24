test = input("Digite algo: ")

print('É um', type(test))
print('É um alfabeto? ', test.isalpha())
print('É um número? ', test.isnumeric())
print('É um alfanumérico? ', test.isalnum())
print('Está em maiúscula? ', test.isupper())
print('Tem espaço? ', test.isspace())

