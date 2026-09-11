# Faça um programa que tenha um função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
# - Quantidade de notas - A maior nota - A menor nota - A média da turma - A situação (opcional) | Adicione também as docstrings da função.

def notas(*nota, sit=False):
    '''
    Função notas() recebe e calculca
    :param nota: recebe todas as notas do alunos
    :param sit: exibe ou não a situação do aluno
    '''
    alunos = {} 

    quantidade = len(nota)
    media = sum(nota) / quantidade
    maior = max(nota)
    menor = min(nota)

    alunos["Total"] = quantidade
    alunos["Maior nota"] = maior
    alunos["Menor nota"] = menor
    alunos["Média"] = media

    if sit == True:
        if media < 5:
            alunos["Situação"] = "Ruim"
        elif media <= 7:
            alunos["Situação"] = "Normal"
        else:
            alunos["Situação"] = "Boa"

    return(alunos)


resp = notas(9, 10, 5.5, 2.5, 8.5, sit=True)
print("-"*60)
print(resp)
#help(notas)