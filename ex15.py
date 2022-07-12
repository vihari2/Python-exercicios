#exercicio faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math

angulo=float(input('Digite o angulo que você deseja: '))
seno=math.sin(math.radians(angulo))
cosseno= math.cos(math.radians(angulo))
tangent= math.tan(math.radians(angulo))

print('o valor de {} em seno será de {:.2f}'.format(angulo,seno))
print('o valor de {} em cosseno será de {:.2f}'.format(angulo, cosseno))
print('o valor de {} em tangente será de {:.2f}'.format (angulo, tangent))
