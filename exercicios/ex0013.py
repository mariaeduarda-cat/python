# Crie um programa que leia a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi
# alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado;


dias = int(input('Quantos dias alugados? '))
Km = int(input('Quantos Km rodados? '))
print(f'O total a pagar é de R${(60*dias)+(0.15*Km):.2f}')