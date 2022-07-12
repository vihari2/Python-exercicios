#exercicio Crie um programa que leia o nome completo de uma pessoa e mostre:

#– O nome com todas as letras maiúsculas e minúsculas.

#– Quantas letras ao todo (sem considerar espaços).

#– Quantas letras tem o primeiro nome.


nome = input('Digite o seu nome completo:').strip()
a = nome.lower()
b = nome.upper()
c = len(nome) - nome.count(' ')
d = nome.find(" ")
print('O nome com todas as letras maiúsculas: {} e minúsculas: {}'.format(b,a))
print('Tem {} letras ao todo (sem considerar espaços).'.format(c))
print('o primeiro nome tem {} letras'.format(d))