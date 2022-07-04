# Crie um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor;


n1 = int(input('Digite um número: '))
ant = n1 - 1
suc = n1 + 1
print('O antecessor de {} é {} e o sucessor é {}'.format(n1, ant, suc))
# Codígo com variáveis e com .format();

n1 = int(input( 'Digite um numero inteiro: '))
print(f'o seu antecessor é {n1 - 1} e o seu sucessor é {n1 + 1}')
# Codígo sem variáveis e com a função .format() simplificada com um f na frente da aspa;

n = int(input('digite um numero:'))
print('a antecesor de {} é {} e seu sucessor é {}'.format(n, n-1, n+1))
# Codígo sem variáveis e com .format();
