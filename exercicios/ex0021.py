# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 'SANTO';

cid = str(input('Em que cidade você naceu? ')).lower().replace('-', '').split()
print('santo' in cid[0:5])

