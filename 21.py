#excercicio crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

cidade = input('digite a cidade: ')).split()
print('a cidade começa com a palavra santo?')
print('santo' in cidade[0].lower()) 

#ou

cidade = input('Em qual cidade você nasceu?  ')
cidade1 = cidade.upper()
cidade2 = cidade1.split()
print('SANTO' in(cidade2[0]))

#ou

cid = input('Em qual cidade vc nasceu? ').strip()
print(cid[:5].upper() == 'SANTO')
