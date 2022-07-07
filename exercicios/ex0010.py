# Crie um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto;


produto = float(input('Qual é o preço do produto? R$'))
print(f'O produto que custava R${produto}, na promoção com desconto de 5% vai custar R${produto * 0.95:.2f}.')
# novo = produto - (produto * 5 / 100)


produto = float(input('Qual é o preço do produto? R$'))
desconto = int(input('De quanto será o desconto? %'))
print(f'O produto que custava R${produto}, na promoção com desconto de {desconto}% vai custar R${produto - (produto * desconto)/100:.2f}.')
# Codígo generalizado; 
