import pandas as pd
import random
import matplotlib.pyplot as plt
from itertools import count
from matplotlib.animation import FuncAnimation

plt.style.use('seaborn-v0_8-paper')


def animate(i):
    dates = pd.read_csv('data_3.csv')
    x = dates['x_value']
    y1 = dates['total_1']
    y2 = dates['total_2']
    plt.cla()
    plt.plot(x, y1, label='Total 1')
    plt.plot(x, y2, label='Total 2')
    plt.legend(loc='upper left')
    plt.tight_layout()


ani = FuncAnimation(plt.gcf(), animate, interval=1000)
data = pd.read_csv('data_3.csv')
plt.show()
# x_values = []
# y_values = []
# index = count()
# def animate(i):
#     x_values.append(next(index))
#     y_values.append(random.randint(0, 5))
#     plt.cla()
#     plt.plot(x_values, y_values)
# ani = FuncAnimation(plt.gcf(), animate, interval=1000)
# plt.tight_layout()
# plt.show()
