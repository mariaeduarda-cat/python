# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado;
# A multa vai custar R$7,00 por cada Km acima do limite;


print("LIMITE DE VELOCIDADE DA VIA: 80KM/H \n---MULTA DE R$7,00 PARA CADA KM ACIMA DO LIMITE---\n")
kil = int(input("Velocidade do seu carro: "))
mult = (kil - 80) * 7

if kil > 80:
    print(f'Você ultrapassou o limite de velocidade, page a multa referente à: R${mult}')
else:
    print('Você está no limite da via. Tenha uma boa viagem!!!')