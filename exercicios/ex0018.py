# O mesmo professor do exercício anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Crie um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.


n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
alunosx = [n1, n2, n3, n4]
alunos = sorted(alunosx)
print(f'A ordem de apresentação será: \n{alunos}')
# Uma maneira alternativa desse exercício seria o comando 'sorted()' que neste caso também escolhe nomes aleatórios. A função tem o objetivo de ordenar as informações de uma determinada lista. EX: sorted([5, 2, 3, 1, 4]) >>> [1, 2, 3, 4, 5];

from random import shuffle

n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
alunosx = [n1, n2, n3, n4]
shuffle(alunosx)
print(f'A ordem de apresentação será: \n{alunosx}')
# Do módulo 'random' usamos a função 'shuffle' para embaralhar os elementos de uma lista;

from random import sample
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
alunosx = [n1, n2, n3, n4]
ordem = sample(alunosx, k=4)
print(f'A ordem de apresentação será: \n{ordem}')
# Outra função do módulo 'random' seria o 'sample(population, k=x)' que diferentemente do shuffle que também embaralha os elementos de uma lista, podemos também limitar a quantidade de elementos, em que nenhum deles se repete; 
# A 'population' que deve ser informada é o array e o 'k' é o número de elementos do array que se deseja escolher aleatoriamente;
# f'Os alunos escolhidos foram {sample([n1, n2, n3 ,n4], 2)', outra forma economizando código, também o 'k=x' não é obrigatório;

cor = random.sample(['red', 'blue', 'green'], count = [3, 4, 1], k=8)
print(cor)
# Elementos repetidos podem ser especificados um de cada vez ou com o parâmetro somente-nomeado opcional count(s). sample(x, count[], k)

import random

nome = str(input('Primeiro aluno: '))
nome = input('Segundo aluno: ')
nome = input('Terceiro aluno: ')
nome = input('Quarto aluno: ')
lista = [nome, nome, nome, nome]
escolhido = random.choices(lista, k=4)
print(f'O aluno escolhido foi {escolhido}')
# A função 'choices(population, k=x)' que também pede um índice 'k' chama uma quantidade k de elementos, podendo eles serem repetidos ou não. 

