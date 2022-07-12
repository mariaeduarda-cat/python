# Crie um programa que leia umm número real qualquer e mostre na tela a sua porção inteira;

# TRABALHANDO COM IMPORTANÇÕES;


import math
# A função 'import x' importará a biblioteca inteira de algum modúlo;

n = float(input('Digite um número: '))
print(f'A porção inteira deste número é {math.trunc(n)}')
# Depois da função 'import math' importar todas as funções matemáticas de math, usamos 'math.trunc()' que serve para remover as partes decimais(quebrar) de um número e retornar apenas a parte inteira, math.x();

from math import trunc
# A função 'from x import y' serve para importar apenas um elemento específico de um módulo qualquer, neste caso a biblioteca 'math' e a função 'trunc()', sem a necessidade de colocar novamente o math apenas a função trunc();

n = float(input('Digite um número: '))
print(f'A porção inteira deste número é {trunc(n)}')

n = float(input('Digite um número: '))
print(f'A porção inteira deste número é {int(n)}')
# Outra maneira de conseguir a porção inteira;

# Podemos dar apelidos as funções da biblioteca, no intuito de ser mais fácil de se compreender. Por exemplo:
# Utilizando 'as' podemos dar um apelido a alguma função da biblioteca. Vejamos com o sqrt:
# from math import sqrt as raizquadrada
# agora ao invés de usar 'sqrt(4)' ou 'math.sqrt(4)', podemos usar 'raizquadrada(4)', assim o resultado será o mesmo e retornará 2;

from math import sqrt as rq

num = int(input('Digite um número: '))
print(f'A raiz quadrada deste número é: {rq(num)}')