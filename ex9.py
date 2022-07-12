# exercicio  faça um programa q leia a altura e a largura de uma parede em metros, calcule
# a sua área e a quantidade de tinta necessaria para pintá-la , sabendo que cada
# litro de tinta pinta uma área de 2m². 


a = float(input('ql é a altura da parede em metros:'))
b = float(input('ql é a largura da parede em metros:'))
s = a * b
x = s / 2 


print ('a área da parede é {} metros quadrados, e a parede precisará de {} latas de tinta' .format(s,x))
