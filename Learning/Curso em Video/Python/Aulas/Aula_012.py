nome = str(input('Qual é seu nome? '))
if nome == 'Gustavo':
    print('Que nome bonito! ')
elif nome == 'Gabriel' or nome == 'Marcelo':
    print('Que nome de gay')
else:
    print('Seu nome é um bom nome, eu teria esse nome, você teria esse nome?')
print('Tenha um bom dia, {}'.format(nome))