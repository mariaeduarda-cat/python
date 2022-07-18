# Faça um programa que leia na tela um número de 0  a 9999 e mostre na tela cada um de seus dígitos separados;
# EX: Digite um número: 1567
# unidade: 7 dezena: 6 centena: 5 milhar: 1;


num = int(input('Insira um número: '))
u = (num // 1) % 10
d = (num // 10) % 10
c = (num // 100) % 10
m = (num // 1000) % 10
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
# Para entender melhor este problema podemos divídi-los em partes; EX:
# Divisão: 1234 / 10 = 123,4
# Divisão inteira: 1234 // 10 = 123
# Módulo: 1234 % 10 = 4 (o resto da divisão)
# Pra descobrir a centena fazemos a divisão inteira por 100: 1234 // 100 = 12
# Depois pegamos o resultado e dividimos por 10, mas pega só o resto dessa divisão (que é o módulo): 12 % 10 = 2. Ou seja, a centena é 2.

num = int(input('Insira um número: '))
n = str(num)
print('Unidade: {}'.format(n[3]))
print('Dezena: {}'.format(n[2]))
print('Centena: {}'.format(n[1]))
print('Milhar: {}'.format(n[0]))
# Dividir os dígitos com método de string, porém com erro se não usarmos os 4 dígitos então não é a melhor maneira