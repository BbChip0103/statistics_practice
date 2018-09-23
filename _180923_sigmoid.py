import math
import matplotlib.pyplot as plt

### 여기서 bx+a => wx+b
### a는 변곡선이 꺾이는 중심을 의미, b는 변곡선의 기울기를 의미
def sigmoid(x, a=0, b=1):
    return 1 / (1 + math.exp(-1*(a + b*x)))

### a와 b 사이의 범위를 가지고, c는 변곡선의 기울기를, d는 변곡선의 중심을 의미
def sigmoid(x, a=0, b=1, c=1, d=0):
    return a + ((b-a) / (1 + math.exp(c * (d-x))))

if __name__=='__main__':
    # for i in range(6):
    #     print(f_N(i, 0, 1))

    plt.figure(0)

    # for numb in range(10):
    #     plt.subplot(5, 2, numb+1)
    #     x_range = [0.1*i for i in range(-120, 120)]
    #     y_range = [sigmoid(i, 0, numb*0.5-2.5) for i in x_range]
    #     plt.plot(x_range, y_range)
    #     plt.title('sigmoid(i, 0, {})'.format(numb*0.5-2.5))

    for numb in range(-5 , 5):
        plt.subplot(5, 2, numb+6)
        x_range = [0.1*i for i in range(-120, 120)]
        y_range = [sigmoid(i, a=0, b=1, c=1, d=numb) for i in x_range]
        plt.plot(x_range, y_range)
        plt.title('sigmoid(i, a=0, b=1, c=1, d={})'.format(numb))


    plt.tight_layout()
    plt.show()
