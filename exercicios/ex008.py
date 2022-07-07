# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar;


num = float(input('Quanto dinheiro você tem na carteira? R$'))
print(f'Com R${num} você pode comprar U${num/5.34:.2f} \nE consequentemente: \n€{num/5.43:.2f} \n¥{num/0.039:.2f} \n₩{num/0.0041:.2f} \n£{num/6.42:.2f}')

