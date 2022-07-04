# Crie um programa que converta as escalas de temperaturas(celsius, kelvin e farenheit) entre si;


temp = float(input('Informe a temperatura em ºC: '))
print(f'A temperatura de {temp}º corresponde a {(temp*1.8)+32:.2f}Fº e em Kelvin {temp+273.15:.2f}Kº.')
temp = float(input('Informe a temperatura em ºK: '))
print(f'A temperatura de {temp}º corresponde a {temp-273.15:.2f}Cº e em Farenheit {(temp-273.15)*9/5+32:.2f}Fº.')
temp = float(input('Informe a temperatura em ºF: '))
print(f'A temperatura de {temp}º corresponde a {(temp-32)*5/9:.2f}Cº e em Kelvin {(temp-32)*5/9+273.15:.2f}Fº.')