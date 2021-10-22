from sympy import *
x=Symbol('x')

y = integrate(x**2, (x, -1, 1))  
print(y)
print(y.evalf())

y = integrate(sin(x), (x, 0, pi/2)) 
print(y)
