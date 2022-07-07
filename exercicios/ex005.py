# Crie um programa que leia as duas notas de um aluno, calcule e mostre a sua média;



n1 = int(input('Nota da 1º prova: '))
n2 = int(input('Nota da 2º prova: '))
media = (n1 + n2) / 2
print('A média da prova 1 e da prova 2 é de {:.1f}'.format(media))

n1 = float(input('Nota da 1º prova: '))
n2 = float(input('Nota da 2º prova: '))
print('A média entre {} e {} é {:.1f}'.format(n1, n2, (n1 + n2) / 2))

n1 = float(input('Nota da 1º prova: '))
n2 = float(input('Nota da 2º prova: '))
print('> Nota final: {} \n> Média: {:.1f}'.format(n1 + n2, (n1 + n2) / 2))