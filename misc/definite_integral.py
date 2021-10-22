from sympy import *
x=Symbol('x')

# This calculates the definite integral of y=x^2 from -1 to 1
y = integrate(x**2, (x, -1, 1))  
print(y)
print(y.evalf())

# This calculates the definite integral of y=sin(x) from 0 to pi/2
y = integrate(sin(x), (x, 0, pi/2)) 
print(y)
