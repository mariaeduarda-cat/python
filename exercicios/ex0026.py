# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador;
# O programa deverá escrever na tela se o usuário venceu ou perdeu;


import random

num = random.random()
print(f'O número escolhido foi {num}')
# random.random() me retorna um número flot aleatório entre 0.0 e 1.0;

from random import randint

num = float(input('Digite um numero entre 0 e 5: '))
comp = randint(0, 5)
print(f'O número escolhido pelo computador foi {comp}')

if num == comp:
    print('Você venceu. PARABÉNS!!')
else:
    print('Você perdeu. TENTE NOVAMENTE!!')
# random.randint(a, b) me retorna um número aleatório inteiro entre os dois números passados pelo parâmetro;