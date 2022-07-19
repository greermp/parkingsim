import matplotlib.pyplot as plt
import numpy as np
import itertools
import math
from matplotlib.widgets import Button

fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.2)


def plotParking(targets, ratio, xspace, yspace, effectArea):

    cols=math.ceil(math.sqrt(targets))
    rows=math.ceil(targets/cols)



    r = cols*xspace
    c = rows*yspace
    x = np.linspace(0, c, int(c/100+1))
    y = np.linspace(0, r, int(r/100+1))

    pts = itertools.product(x, y)
    ax.scatter(*zip(*pts), marker='o', s=30, color='red')


    # N = 10
    # x = np.random.rand(N)
    # y = np.random.rand(N)
    # colors = np.random.rand(N)
    # area = np.pi * 0.2
    # l = ax.scatter(x, y, s=area, c=colors, alpha=0.8)


    def gen(event):
        N = 10
        x = np.random.randint(0,(c+100)/100)*100
        y = np.random.randint(0,(r+100)/100)*100
        # colors = np.random.rand(N)
        # area = np.pi * effectArea**2
        
        circle1 = plt.Circle((x, y), effectArea, color='r', fill=False)
        ax.add_patch(circle1)
        # ax.scatter(x, y, s=area, c='red', alpha=0.2)
        plt.draw()


    axgen = plt.axes([0.81, 0.05, 0.1, 0.075])
    bgen = Button(axgen, 'Generate')
    bgen.on_clicked(gen)


    plt.show()
    
    
targets = 8
ratio = 2
xspace  = 100
yspace = 100
effectArea = 100

plotParking(100, 2, 100, 100, 150)
