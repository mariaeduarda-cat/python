n1 = float(input('Digite seu salário: '))
amt = n1 * 1.15
print('Seu novo salário com 15°/° de aumento é de {}'.format(amt))

n1 = float(input('Digite o valor do produto: '))
desc = n1 * 0.95
print('O novo preço deste pproduto com 5°/° de desconto é {:.2f}'.format(desc))

n1 = float(input('Qual a largura da parede? '))
n2 = float(input('Qual a altura da parede? '))
area = n1 * n2
print('A área dessa parede é de: {}'.format(area))
print('Para pintar toda a parede você precisará de {}L de tinta'.format(area / 2))


n1 = int(input('Quanto dinheiro tem sua carteira? '))
dolar = n1 / 5,34
print(f'Com este dinheiro você consegue comprar {dolar:.2f} dólares')

n1 = int(input('Digite um número para ver seu sucessor e seu antecessor: '))
print('O antecessor de {} é {}\nE o sucessor é {}'. format(n1, n1 - 1, n1 + 1))

n1 = int(input('Digite um número para ver o seu dobro, triplo e raiz quadrada: '))
print(f'O dobro de {n1} é {n1*2}\nO triplo é {n1*3}\nA raiz quadrada é {n1**(1/5)}')


n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
print(f'O total é: {n1 + n2}\nE a média é {media:.2f}')


n1 = float(input('Digite um valor em metros: '))
cn = n1 * 100
mm = n1 * 1000
print('O valor digitado convertido para centímetros é {}\nE é milímetros é {}'.format(cn, mm))


n1 = int(input('Digite um número para ver sua tabuada: '))
print(f'{n1} x 1 = {n1 * 1}')
print(f'{n1} x 2 = {n1 * 2}')
print(f'{n1} x 3 = {n1 * 3}')
print(f'{n1} x 4 = {n1 * 4}')
print(f'{n1} x 5 = {n1 * 5}')
print(f'{n1} x 6 = {n1 * 6}')
print(f'{n1} x 7 = {n1 * 7}')
print(f'{n1} x 8 = {n1 * 8}')
print(f'{n1} x 9 = {n1 * 9}')
print(f'{n1} x 10 = {n1 * 10}')
