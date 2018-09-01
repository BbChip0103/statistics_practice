import math
import matplotlib.pyplot as plt
from _180826_math_test import f_Binom

def f_N(x, mu, sigma):
    return (1 / (math.sqrt(2*math.pi) * sigma)) \
            * (math.exp(-1*((x-mu)**2) / 2*(sigma**2)))

def f_EXP(x, _lambda):
    return (1/_lambda) * math.exp(-1*x / _lambda)

if __name__=='__main__':
    # for i in range(6):
    #     print(f_N(i, 0, 1))

    def EXP_test():
        plt.figure(0)

        for i in range(1, 11):
            plt.subplot(5, 2, i)
            x_range = [0.1*j for j in range(-100, 100)]
            y_range = [f_EXP(j, 0.5*i) for j in x_range]
            plt.plot(x_range, y_range)
            plt.title('EXP({})'.format(0.5*i))
            print(sum(y_range))

        plt.tight_layout()
        plt.show()

    EXP_test()

    def CLT_test():
        plt.figure(0)

        for i in range(1, 10):
            plt.subplot(5, 2, i)
            plt.plot([f_Binom(x, 10*i, 0.5) for x in range(10*i)])
            plt.title('B({}, 0.5)'.format(10*i))
            print(sum([f_Binom(x, 10*i, 0.5) for x in range(10*i)]))

        plt.subplot(5, 2, 10)
        x_range = [0.1*i for i in range(-100, 100)]
        y_range = [f_N(i, 0, 1) for i in x_range]
        plt.plot(x_range, y_range)
        plt.title('N(0, 1)')
        print(sum(y_range))

        plt.tight_layout()
        plt.show()
