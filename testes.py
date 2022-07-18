num = int(input('Digite um número de 0 até 9999: '))
print(f'Número digitado {num}')
print(f'Unidade: {(num // 1) % 10 }')
print(f'Dezena: {(num // 10) % 10}')
print(f'Centena: {(num // 100) % 10}')
print(f'Milhar: {(num // 1000) % 10}')

cidade = str(input('Qual o nome da sua cidade? '))
print('Sua cidade começa com Santo? {}'.format('Santo' in cidade))


nome = str(input('Qual o seu nome? '))
slv = 'Silva' in nome
print(f'Seu nome tem Silva? {slv}')

cidade = str(input('Qual o nome da sua cidade? '))
print('Sua cidade começa com Santo? {}'.format('Santo' in cidade))