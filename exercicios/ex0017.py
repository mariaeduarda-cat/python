# Um professor que sortear um de seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles
# e escrevendo um nome do escolhido;


import random
nome = input('Primeiro aluno: ')
nome = input('Segundo aluno: ')
nome = input('Terceiro aluno: ')
nome = input('Quarto aluno: ')
lista = [nome, nome, nome, nome]
escolhido = random.choice(lista)
print(f'O aluno escolhido foi {escolhido}')
# Do módulo 'random' usamos a função 'choice' para escolher um item aleátorio de uma [lista] = array;
