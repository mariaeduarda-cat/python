# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raíz quadrada;



n1 = int(input('Digite um número: '))
d = n1 * 2
t = n1 * 3
rq = n1 ** (1/2)
print('O dobro de {} é {}. \nO triplo é {}. \nE a raiz quadrada é {:.3}'.format(n1, d, t, rq))
# Codígo com variáveis e .format();

n1 = int(input('Digite um número: '))
print('> O dobro de {} vale {}. \n> O triplo vale {}. \n> E a raiz quadrada vale {:.2f}.'.format(n1, n1*2, n1*3, pow(n1, 1/2)))
# Codígo sem variáveis com .format() e com nova função de quebra de linhas entre um print e outro (\n);
# :.xf é usado para definir a quantidade x de casas decimais;
# Af função pow(x, y) é uma função de potências (base, expoente);


