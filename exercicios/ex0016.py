# Crie um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo;


import math
an = float(input('Qual angulo voce deseja? '))
sen = math.sin(math.radians(an))
cos = math.cos(math.radians(an))
tan = math.tan(math.radians(an))
print(f'O sen de {an} é {sen:.2f} \nO cosseno é {cos:.2f} \nE a tangente é {tan:.2f} ')
# As funções 'math.sin', 'math.cos' e 'math.tan' retornam respectivamente seus angulos dentro de um arco trigonometro.
# Porém sendo necessário o uso da função 'math.radians' para retornar o angulo de radianos em graus;

