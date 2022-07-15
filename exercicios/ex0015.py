# Crie um programa que leia o comprimento do cateto oposto e do cacteto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa;


co = float(input('Quanto mede o cateto oposto? '))
ca = float(input('Quanto mede o cateto adjacente? '))
hi = (co**2 + ca**2) ** (1/2)
print(f'A hipotenusa vai medir {hi:.2f}')
# Codígo resolvido da maneira matemática sem importação;
# h² = co² + ca²

from math import hypot

co = float(input('Quanto mede o cateto oposto? '))
ca = float(input('Quanto mede o cateto adjacente? '))
hi = hypot(co, ca)
print('A hipotenusa deste triangulo mede {:.2f}'.format(hi))
# A função 'hypot()' é usada para calcular a hipotenusa;

import math

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = math.sqrt((pow(co, 2) + pow(ca, 2)))
print('A hipotenusa vai medir {:.2f}'.format(hi))
# A função 'math.sqrt' retorna a raiz quadrada de um número;