#exercicio faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

import math

co=float(input('Digite o comprimento do cateto oposto: '))

ca=float(input('Digite o comprimento do cateto adjacente: '))

h = math.hypot(co,ca)

print('o comprimento da hipotenusa é {:.2f}'.format(h))

#ou opção s/ import 

co=float(input('Digite o comprimento do cateto oposto: '))

ca=float(input('Digite o comprimento do cateto adjacente: '))

h = (co**2) + (ca**2) ** (1/2)

print('o comprimento da hipotenusa é {:.2f}'.format(h))
