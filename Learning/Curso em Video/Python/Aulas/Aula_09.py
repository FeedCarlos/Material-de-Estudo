frase = "Curso em Vídeo Python"

print('''AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
      AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAa''')

# Fatiamento

# Corta a frase e pula na seguinte sequencia: inicio, final, salto
print(frase[1:15:2])

# Transformação

print(frase)

# Tamanho da frase
print(len(frase))
# Quantos 'o' na frase
print(frase.count('o'))
# Encontra a palavra
print(frase.find('deo'))
print(frase.find('Android'))
# Pergunta se tem na frase
print('Curso' in frase)
# Realoca uma palavra
print(frase.replace('Python', 'Android'))
# Colocar todas as minúsculas para maiúsculas
print(frase.upper())
# Coloca todas as maiúsculas para minúsculas
print(frase.lower())
# Coloca a primeira letra da frase em maiúscula
print(frase.capitalize())
# Coloca todos os inicios de palavra em maiúscula
print(frase.title())
# Remove espaços do inicio e final
print(frase.strip())
# Remove espaço apenas da direita
print(frase.rstrip())
# Remove espaço apenas da esquerda
print(frase.lstrip())

# Divisão

# Divide uma string para uma lista
print(frase.split())

# Junção 

# Para juntar 
print('-'.join(frase))