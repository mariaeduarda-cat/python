# Crie um programa que converta as escalas de temperaturas(celsius, kelvin e fahrenheit) entre si;


temp = float(input('Informe a temperatura em °C: '))
print(f'A temperatura de {temp}° corresponde a {(temp * 1.8) + 32:.2f}°F e em Kelvin {temp + 273:.2f}K.')

temp = float(input('Informe a temperatura em °K: '))
print(f'A temperatura de {temp}K corresponde a {temp - 273:.2f}°C e em Fahrenheit {(temp-273) * 9/5 + 32:.2f}°F.')

temp = float(input('Informe a temperatura em °F: '))
print(f'A temperatura de {temp}° corresponde a {(temp - 32) * 5/9:.2f}°C e em Kelvin {(temp - 32) * 5/9 + 273:.2f}K.')