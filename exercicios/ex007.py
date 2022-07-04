# Crie um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada;

n = int(input('Digite um número: '))
print('A tabuada de {} é: '.format(n), end='')
print('\n{} \n{} \n{} \n{} \n{} \n{} \n{} \n{} \n{} \n{}'.format(n*1, n*2, n*3, n*4, n*5, n*6, n*7, n*8, n*9, n*10))

n = int(input('Digite um número: '))
print('A tabuada de {} é: '.format(n), end='')
print(f'\n{n*1} \n{n*2} \n{n*3} \n{n*4} \n{n*5} \n{n*6} \n{n*7} \n{n*8} \n{n*9} \n{n*10}')
# Uma forma rápida de usar o .format() é colocar apenas um f em frente a aspa do print e solucionar o problema dentro das chaves;

n = int(input('Digite um número para ver sua tabuada: '))
print('-' * 20)
print('{} x {:2} = {}'.format(n, 1, n*1))
print('{} x {:2} = {}'.format(n, 2, n*2))
print('{} x {:2} = {}'.format(n, 3, n*3))
print('{} x {:2} = {}'.format(n, 4, n*4))
print('{} x {:2} = {}'.format(n, 5, n*5))
print('{} x {:2} = {}'.format(n, 6, n*6))
print('{} x {:2} = {}'.format(n, 7, n*7))
print('{} x {:2} = {}'.format(n, 8, n*8))
print('{} x {:2} = {}'.format(n, 9, n*9))
print('{} x {:2} = {}'.format(n, 10, n*10))
print('-' * 20)