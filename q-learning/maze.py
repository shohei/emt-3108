import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np
import pdb 
TREASURE = 10

class Maze():
    def __init__(self, x_size, y_size):
        self.map = np.zeros((x_size,y_size))
        for i in range(x_size):
            for j in range(y_size):
                if i==0 or j==0 or i==(x_size-1) or j==(y_size-1):
                    self.map[i][j] = -1
                else:
                    self.map[i][j] = 0

        self.map[2][2] = -1
        self.map[3][2] = -1
        self.map[6][3] = -1
        self.map[7][3] = -1
        self.map[8][3] = -1
        self.map[2][6] = -1
        self.map[2][7] = -1
        self.map[3][6] = -1
        self.map[6][7] = -1

        # Reward
        self.map[8][6] = TREASURE

        # Create state number array
        self.number = np.zeros_like(self.map)
        for i in range(x_size):
            for j in range(y_size):
                s = self.xy2s(i,j,x_size)
                self.number[i][j] = s

    def xy2s(self, x, y, x_size):
        s = x + y * x_size
        return s

    def move(self, a, x, y, x_size):
        if a==0:
            y += 1
        elif a==1:
            x += 1
        elif a==2:
            y -= 1
        elif a==3:
            x -= 1
        s2 = self.xy2s(x, y, x_size)
        return x, y, s2

    def plot(self, x_size, y_size):
        cmap = colors.ListedColormap(['black', 'white', 'yellow'])
        bounds = [-2,-0.1,0.1,TREASURE+1]
        norm = colors.BoundaryNorm(bounds, cmap.N)
        _, ax = plt.subplots()
        ax.imshow(self.map, cmap=cmap, norm=norm)
        ax.grid(which='major', axis='both', linestyle='-', color='k', linewidth=2)
        ax.set_xticks(np.arange(-.5, y_size, 1));
        ax.set_yticks(np.arange(-.5, x_size, 1));
        ax.xaxis.set_ticklabels([])
        ax.yaxis.set_ticklabels([])
        plt.show(block=False)
    