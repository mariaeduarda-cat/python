# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O NOME COM TODAS AS LETRAS MAIÚSCULAS;
# O NOME COM TAS AS LETRAS MINÚSCULAS;
# QUANTAS LETRAS AO TODO (SEM CONSIDERAR OS ESPAÇOS);
# QUANTAS LETRAS TEM O PRIMEIRO NOME;


nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print(f'Seu nome em maiúculas é {nome.upper()}')
print(f'Seu nome em minúsculas é {nome.lower()}')
print('Seu nome tem ao todo {} letras'.format(len(nome) - (nome.count(' '))))
print(f'Seu primeiro nome é {nome[0:5]} e ele tem {len(nome[0:5])} letras')
# Uma forma de contar todas as letras sem contar os espaços é usando len(nome) - (nome.count(' '), pois assim o codígo
# irá contar todas as letras sem contar com os espaços entre as palavras;

print('Seu primeiro nome tem {}'.format(nome.find(' ')))
# Outra forma de achar quantas letras tem o primeiro nome é usando nome.find(' ') pois assim o codígo irá encontrar
# o primeiro espaço;

print(len(nome.replace(' ', '')))
# Também podemos usar a função '.replace()' para substituir um espaço vazio por uma string vazia;

separa = nome.split()
print(separa)
print('Seu primeiro nome tem {} letras'.format(len(separa[0])))
# Uma maneira talvez mais simples seria a função 'split()';
