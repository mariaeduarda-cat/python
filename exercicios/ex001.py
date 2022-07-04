# Crie um programa que leia dois números e mostre a soma, multiplicção, divisão, divisão inteira e a potência entre eles;


n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, o produto é {} e a divisão é {:.2f}'.format(s, m, d), end=' >>> ')
# A funçao end='' tem como objetivo dar continuidade a um print sem quebra de linha;
# :.xf é usado para definir a quantidade x de casas decimais;

print('Divisao inteira {} e potencia {}'.format(di, e))