from math import sqrt

Print('Vamos fazer uma raiz Quadrada')
a = int(input(Insira o valor de a:))
b = int(input(Insira o valor de a:))
c = int(input(Insira o valor de a:))

delta = b**2 - 4*a*c
x1 = (-b +sqrt(delta))/(2*a)
x2 = (-b -sqrt(delta))/(2*a)
print(f'Raizes: X1={x1}, X2: {x2})

