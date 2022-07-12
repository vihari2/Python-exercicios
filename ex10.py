#exercicio um algoritmo que leia o salario do funcionario e mostre o seu salario, com 15% de aumento.

s=float(input('digite aqui o salario do funcionario:'))

ns = s * 0.15

sf = s + ns

print('o salario do funcionario com 15% de aumento é de {} reais'.format (sf))
