#exercicio escreva um programa que pergunte a quantidade de Km percorridos
#por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
#Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

a = int(input('quantos dias vc alugou o carro?'))
b = float(input('qual foi a quantidade km percorridos?'))

p = (a * 60)+(0.15 * b)

print ('o total a pagar será de {} reais '.format(p))
