# O mesmo professor do exercício anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Crie um programa que leia
# o nome dos quatro alunos e mostre a ordem sorteada.


n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
alunosx = [n1, n2, n3, n4]
alunos = sorted(alunosx)
print(f'A ordem de apresentação será: \n{alunos}')
# Uma maneira de resolução desse exercício seria o comando 'sorted()' que tem o objetivo de ordenar as informações de uma
# determinada lista. EX: sorted([5, 2, 3, 1, 4]) >>> [1, 2, 3, 4, 5];

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
sample(alunosx, k=4)
print(f'A ordem de apresentação será: \n{alunosx}')
# Outra função do módulo 'random' seria o 'sample' que transforma uma string em uma lista e depois embaralha essa lista.
# A população que deve ser informada é a string e o k é o número de caracteres da string que se deseja escolher aleatoriamente.

