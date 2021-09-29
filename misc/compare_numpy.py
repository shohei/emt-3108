import numpy as np
from timeit import timeit

python_list = [i for i in range(1000000)]
print(timeit(lambda :[i**2 for i in python_list], number=1))

numpy_array = np.array([i for i in range(1000000)])
print(timeit(lambda: np.square(numpy_array), number=1))