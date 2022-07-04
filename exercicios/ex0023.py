# Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra A;
# Em que posição ela aparece na primeira vez;
# Em que posiçao ela aparece na útilma vez;


frase = str(input('Digite uma frase: ')).strip().upper()
print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
print('A primeira posição da letra A aparece na {} posição'.format(frase.find('A')+1))
# Usamos o find()+1 pois na linguagem python ele começa a frase do 0, porém queremos que conte do 1;
print('A ultima posição da letra A aparece na {} posição'.format(frase.rfind('A')+1))
# A função rfind()+1 retorna a posição da última ocorrência da string;