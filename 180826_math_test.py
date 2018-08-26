import math
import matplotlib.pyplot as plt

def f_nCx(n, x):
    return math.factorial(n) / (math.factorial(x) * math.factorial(n-x))

def f_Binom(x, n, p):
    return f_nCx(n, x) * math.pow(p, x) * math.pow(1-p, n-x)

def f_POI(x, _lambda=1):
    return math.exp(-_lambda) * math.pow(_lambda, x) / math.factorial(x)


if __name__=='__main__':
    # for i in range(6):
        # print(f_POI(i, 1))
        # print(f_Binom(50, i, 0.02))

    x = 6

    # Visualization
    plt.figure(0)

    plt.subplot(5, 1, 1)
    plt.plot([f_Binom(i, 5, 0.2) for i in range(x)])
    plt.title('B(5, 0.2)')

    plt.subplot(5, 1, 2)
    plt.plot([f_Binom(i, 10, 0.1) for i in range(x)])
    plt.title('B(10, 0.1)')

    plt.subplot(5, 1, 3)
    plt.plot([f_Binom(i, 50, 0.02) for i in range(x)])
    plt.title('B(50, 0.02)')

    plt.subplot(5, 1, 4)
    plt.plot([f_Binom(i, 200, 0.005) for i in range(x)])
    plt.title('B(200, 0.005)')

    plt.subplot(5, 1, 5)
    plt.plot([f_POI(i, 1) for i in range(x)])
    plt.title('POI(1)')

    plt.tight_layout()
    plt.show()
