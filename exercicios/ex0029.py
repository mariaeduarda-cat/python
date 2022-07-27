# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas;


print('AVISO: \n---VIAGENS DE ATÉ 200KM SÃO COBRADOS R$0,50 POR KM RODADOS---\n---VIAGENS ACIMA DE 200KM SÃO COBRADOS R$0,50 POR KM RODADOS---\n')
km = int(input('Qual a distância da sua viagem em kilômetros? '))
pas = (km - 200) * 0.45
pas2 = (km + 200) * 0.50

if km > 200:
    print(f'O valor da sua passagem é de R${pas}')
else:
    print(f'O valor da sua passagem é de R${pas2}')