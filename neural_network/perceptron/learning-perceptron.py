import random
import pdb

class Perceptron():
    def __init__(self):
        self.w1 = random.random()
        self.w2 = random.random()
        self.theta = random.random()
    
    def forward(self, x1, x2):
        a = self.w1*x1 + self.w2*x2
        if a>self.theta:
            y = 1
        else:
            y = 0
        return y

p = Perceptron()

truth_table = [(0,0,0),(0,1,0),(1,0,0),(1,1,1)] #AND
# truth_table = [(0,0,0),(0,1,1),(1,0,1),(1,1,1)] #OR
# truth_table = [(0,0,1),(0,1,1),(1,0,1),(1,1,0)] #NAND
epsilon = 1e-5
max_error = 1000
dtheta = 0.1
dw1 = 0.1
dw2 = 0.1
while max_error>epsilon:
    errors = []
    for t in truth_table:
        x1 = t[0]
        x2 = t[1]
        r = t[2]
        y = p.forward(x1,x2)
        error = abs(y-r)
        if y==0 and r==1:
            p.theta -= dtheta 
            if x1==1:
                p.w1 += dw1
            if x2==1:
                p.w2 += dw2
        if y==1 and r==0:
            p.theta += dtheta 
            if x1==1:
                p.w1 -= dw1
            if x2==1:
                p.w2 -= dw2
        errors.append(error)
    print("errors",errors)
    max_error = max(errors) 

print("w1:",p.w1,"w2:",p.w2,"theta:",p.theta)
