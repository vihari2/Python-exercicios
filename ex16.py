#exercicio um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

#coloca lista em []

import random
n1=input('Informe o 1.º nome do aluno: ')
n2=input('Informe o 2.º nome do aluno: ')
n3=input('Informe o 3.º nome do aluno: ')
n4=input('Informe o 4.º nome do aluno: ')
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)

print('O escolhido foi {}'.format(escolhido))
