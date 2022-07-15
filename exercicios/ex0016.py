# Crie um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo;


import math
an = float(input('Qual ângulo você deseja? '))
sen = math.sin(math.radians(an))
cos = math.cos(math.radians(an))
tan = math.tan(math.radians(an))
print(f'O seno de {an:.0f}° é: {sen:.2f} \nO cosseno é: {cos:.2f} \nE a tangente é: {tan:.2f} ')
# As funções 'math.sin(x)', 'math.cos(x)' e 'math.tan(x)' retornam respectivamente seus ângulos dentro de um arco trigonomêtro. Porém sendo necessário o uso da função 'math.radians()' para retornar o ângulo de radianos em graus pois o 'x' passado como parâmetro não está em graus centígrados;
# Ou seja, pegamos o ângulo convertemos em radianos e depois com esse ângulo calculamos o seno, cosseno e tangente.

