# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicinário. No final, mostre o conteúdo da estrutura na tela.

bkp = []

test = {
    
}
while True:
    test['Nome'] = str(input("Digite seu nome: "))
    
    test['Media'] = float(input(f"Média de {test['Nome'].capitalize()}: "))
    if test['Media'] < 7:
        test['Situacao'] = 'Recuperação'
    else: 
        test['Situacao'] = 'Aprovado'
    bkp.append(test.copy())
    break
    

#test['Nome'] = "Augusto"
print(bkp)
print(test)
print(test['Nome'])
print(test['Media'])
print(test['Situacao'])