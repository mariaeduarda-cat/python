# Crie um programa que leia umm número real qualquer e mostre na tela a sua porção inteira;


import math
# A função 'import' importa a inteira biblioteca de um modúlo;
n = float(input('Digite um número: '))
print(f'A porção inteira deste número é {math.trunc(n)}')
# Depois da função 'import math' importar todas as funções matemáticas de math, usamos 'math.trunc()' que serve para remover
# as partes decimais de um número e retornar apenas a parte inteira;

from math import trunc
# A função 'from x import y' serve para importar apenas um elemento específico do modúlo math;
n = float(input('Digite um número: '))
print(f'A porção inteira deste número é {trunc(n)}')

n = float(input('Digite um número: '))
print(f'A porção inteira deste número é {int(n)}')

