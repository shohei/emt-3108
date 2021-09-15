from ex06_numerical_diff import numerical_diff

def function_2(x):
    return x[0]**2 + x[1]**2

def func1(x0):
    return x0*x0 + 4.0**2.0

def func2(x1):
    return 3.0**2.0 + x1*x1

print(numerical_diff(func1, 3.0)) # 6.00000000000378
print(numerical_diff(func2, 4.0)) # 7.999999999999119