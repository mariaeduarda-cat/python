# Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra A;
# Em que posição ela aparece na primeira vez;
# Em que posiçao ela aparece na útilma vez;


fr = str(input('Digite uma frase: ')).strip().upper()
frase = fr.replace('Á', 'A').replace('Ã', 'A').replace('Â', 'A').replace('À', 'A')
print(f'A letra A aparece {frase.count("A")+frase.count("Á")+frase.count("Ã")+frase.count("À")+frase.count("Â")} vezes na frase.')
print(f'A primeira letra A apareceu na posição {frase.find("A")+1}')
print(f'A última letra A apareceu na posição {frase.rfind("A")+1}')
# Usamos o find()+1 pois na linguagem python ele começa a contar do 0, porém queremos que começe a contar do 1;
# A função rfind()+1 retorna a posição da última ocorrência da string;