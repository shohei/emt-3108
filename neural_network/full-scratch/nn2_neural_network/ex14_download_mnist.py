import sys, os
sys.path.append(os.pardir) 
from dataset.mnist import load_mnist
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.abspath(os.path.join(os.path.abspath(__file__),"../../")))
sys.path.append(os.path.abspath(os.path.join(os.path.abspath(__file__),"../../../")))

(x_train, t_train), (x_test, t_test) = load_mnist(flatten=True, normalize=False)
print(x_train.shape) # (60000, 784) 
print(t_train.shape) # (60000,) 
print(x_test.shape) # (10000, 784) 
print(t_test.shape) # (10000,)