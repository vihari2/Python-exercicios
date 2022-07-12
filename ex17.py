#exercicio o mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random
n1=input('Informe o 1.º nome do aluno: ')
n2=input('Informe o 2.º nome do aluno: ')
n3=input('Informe o 3.º nome do aluno: ')
n4=input('Informe o 4.º nome do aluno: ')
lista = [n1, n2, n3, n4]
random.shuffle(lista)

print('a ordem da apresentação será {}'.format(lista))
