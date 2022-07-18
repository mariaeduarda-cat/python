# Um professor quer sortear um de seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido;


import random

nome = str(input('Primeiro aluno: '))
nome = input('Segundo aluno: ')
nome = input('Terceiro aluno: ')
nome = input('Quarto aluno: ')
lista = [nome, nome, nome, nome]
escolhido = random.choice(lista)
print(f'O aluno escolhido foi {escolhido}')
# Do módulo 'random' usamos a função 'choice' para escolher somente um elemento aleátorio de uma lista[] que é um array;
# o str(input()) não é obrigatório, mas se quisermos deixar explicítico que se trata de uma string podemos usá-lo;

from random import choice

n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')
lista = [n1, n2, n3, n4]
print(f'O aluno escolhido foi {choice(lista)}')
# Também podemos fazer choice([n1, n2, n3, n4])

