import math
import matplotlib.pyplot as plt
import numpy as np

def f_where_you_go(k, x):
    return -1*(1/k) * math.exp(-1*(k/2) * math.pow(x, 2))


if __name__=='__main__':
    # for i in range(1000):
    #     print(f_where_you_go(0.1, i))



    # Visualization

    x_range = np.arange(-1000, 1000)
    # x = 1000
    plt.figure(0)

    plt.subplot(3, 1, 1)
    plt.plot([f_where_you_go(0.0001, i) for i in x_range])
    plt.title('f_where_you_go(0.01, i) [-1000 <= i < 1000]')

    plt.subplot(3, 1, 2)
    plt.plot([f_where_you_go(0.01, i) for i in x_range])
    plt.title('f_where_you_go(0.1, i) [-1000 <= i < 1000]')

    plt.subplot(3, 1, 3)
    plt.plot([f_where_you_go(1, i) for i in x_range])
    plt.title('f_where_you_go(1, i) [-1000 <= i < 1000]')

    plt.tight_layout()
    plt.show()
