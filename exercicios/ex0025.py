# USO DAS ESTRUTURAS CONDICIONAIS;

# Estrutura condicional composta (com o else);
tempo = int(input('Quantos anos tem seu carro? '))
if tempo <= 3:
    print('carro novo')
else:
    print('carro velho')
print('--FIM--')
# Todo comando que está a esquerda sempre irá acontecer;


# Estrutura condicional simples (sem o else);
nome = str(input('Qual é o seu nome? '))
if nome == 'Gustavo':
    print('Que nome lindo você tem')
print(f'Bom dia, {nome}!')


# Condição simplificada;
tempo = int(input('Quantos anos tem seu carro? '))
print('carro novo' if tempo <= 3 else 'carro velho')
print('--FIM--')

n1 = float(input('Digite a primeira nota: '))
n2 = float(input("Digite a segunda nota: "))
m = (n1 + n2) / 2
print(f'A sua média foi {m:.2f}')

if m>=6:
    print('Você está acima da media! PARABÉNS!!')
else:
    print('Você está abaixo da média! ESTUDE MAIS!!')

# FORMA SIMPLIFICADA:
# print('PARABÉNS!!"' if m>=6 else 'ESTUDE MAIS!!')



