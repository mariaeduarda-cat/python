# Crie um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros;


n1 = int(input('Digite um número em metros: '))
mm = (n1*1000)
cc = (n1*100)
print('O número {} em centímetros é {} e em milímetros é {}'.format(n1, cc, mm))

n1 = int(input('Uma distancia em metros: '))
print('O número {} em centímetros é {} \nE em milímetros é {}'.format(n1, n1*100,n1*1000))

n1 = int(input('Uma distancia em metros: '))
print('A medida de {}m corresponde a: \n{}km \n{}cm \n{}mm \n{}hm \n{}dm'.format(n1, n1/1000, n1*100, n1*1000, n1/100, n1*10))
# Codígo convertido em outras medidas;