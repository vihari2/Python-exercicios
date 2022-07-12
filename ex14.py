#exercicio faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math

angulo=float(input('Digite o angulo que você deseja: '))
seno=math.sin(math.radians(angulo))
cosseno= math.cos(math.radians(angulo))
tangent= math.tan(math.radians(angulo))

print('o valor de {} em seno será de {:.2f}'.format(angulo,seno))
print('o valor de {} em cosseno será de {:.2f}'.format(angulo, cosseno))
print('o valor de {} em tangente será de {:.2f}'.format (angulo, tangent))

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