#exercicio coloque um valor e mostre o dobro, triplo e raiz quadrada. 

x =int (input('digite um valor:'))
d= x * 2
t = x * 3
r = x ** (1/2)

print('dobro de {} vale {}, o triplo de {} vale {} e a raiz de {} vale {:.2f}' .format(x,d,x,t,x,r))