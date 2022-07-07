# Crie um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros;



n1 = float(input('Uma distância em metros: '))
print(f'A medida de {n1:.1f}m corresponde a: \n{n1/1000}km \n{n1/100}hm \n{n1/10}dm \n{n1*10}dm \n{n1*100}cm \n{n1*1000}mm')
# Codígo convertido em outras medidas;

#Tabela das medidas
# KM HM DAM M DM CM MM
#km = kilômetro 
#hm = hectômetro
#dam = decâmetro                 
#m = metro
#dm = decímetro
#cm = centrímetro
#mm = milímetro