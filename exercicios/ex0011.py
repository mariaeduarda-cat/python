# Crie um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com aumento de 15%;


salário = float(input('Qual é o salário do funcionário? R$'))
print(f'O funcionário que ganhava R${salário:.3f}, com aumento de 15%, passa a receber R${salário*1.15:.3f}.')
# novo = salário (salário * 15 / 100)

salário = float(input('Qual é o salário do funcionário? R$'))
aumento = int(input('De quanto será o aumento? %'))
aum = salário + (salário * aumento / 100)
print(f'O funcionário que ganhava R${salário:.2f}, com aumento de {aumento}%, passa a receber R${aum}')

salário = float(input('Qual é o salário do funcionário? R$'))
aumento = int(input('De quanto será o aumento? %'))
print(f'O funcionário que ganhava R${salário:.2f}, com aumento de {aumento}%, passa a receber R${salário + (salário * aumento / 100):.2f}')
klklklk
