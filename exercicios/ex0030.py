# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO;

ano = int(input('Digite um ano: '))
bis = ano % 400 == 0
bis2 = ano % 100 == 0

if ano % 4 == 0 or bis or bis2:
    print(f'{ano} é um ano bissexto!')
else:
    print(f'{ano} não é um ano bissexto')