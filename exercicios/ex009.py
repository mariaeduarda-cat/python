# Crie um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m²;


lar = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
print(f'Sua parede tem a dimensão de {lar}x{alt} e sua área é de {lar*alt}m².\n-Para pintar esta parede, você precisará de {(lar*alt)/2:.2f}l de tinta.')


#Cálculo área: altura * largura(base)
#Perímetro: soma de todos os lados 