from cx_Freeze import setup, Executable
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import math
import numpy as np
import pandas as pd


# Load data from the CSV file
path = 'results.csv'
pathk = 'results1.csv'
df = pd.read_csv(path, sep=';', decimal=',')
df1 = pd.read_csv(pathk, sep=';', decimal=',')


times = list(df['Time'])
times = [time_str.replace(',', '.') for time_str in times]
times = [float(time_str) for time_str in times]
#times = df.iloc[1:, 0].values.astype(float)
x = [float(i.replace(',', '.')) for i in list(df.columns[1:])]

u = df1.iloc[0:, 0].values.astype(float)
d = df1.iloc[0:, 1].values.astype(float)
F_p = df1.iloc[0:, 2].values.astype(float)
F_m = df1.iloc[0:, 3].values.astype(float)


def find_closest_index(lst, target):
    closest = min(lst, key=lambda x: abs(x - target))
    return lst.index(closest)


def function(x, time):
    return math.exp(-math.pi**2*time)*math.sin(math.pi*x)


def update(val):
    time = time_slider.val
    ind = find_closest_index(times, time)

    x1_values = x
    x2_values = np.arange(-1, 1, 0.0001)
    y1_values = list(df.iloc[ind, :])[1:]
    y1_values = [float(y1_str) for y1_str in y1_values]
    y2_values = [function(x, time) for x in x2_values] # для синуса
    #y2_values = [1 - x * x for x in x2_values] # для параболы

    k = []
    b = []
    diff_values = []
    for i in range(len(x) - 1):
        k.append((y1_values[i+1] - y1_values[i]) / (x[i+1] - x[i]))
        b.append(y1_values[i] - ((y1_values[i+1] - y1_values[i]) / (x[i+1] - x[i])) * x[i])

    j = 1
    y3_value = []
    y_diff = 0
    square_norm = 0
    h1 = x1_values[1] - x1_values[0]
    h2 = x1_values[-1] - x1_values[-2]
    for i in range(len(x2_values)):
        if x2_values[i] > x[j]:
            j += 1
        y3_value.append(k[j - 1] * x2_values[i] + b[j - 1]) #Это я считаю, чтоб если у дискретного [-1, 0,-97, -0,94,...,1] посчиталось на прямой между двумя дискретыми точками
        ''' # это чтоб построить график относительных ошибок нужно
        try:
            diff_values.append(abs(y3_value - y2_values[i])/abs(y3_value))
        except:
            diff_values.append(100)
        '''
    for i in range(len(x1_values)):
        if abs(y1_values[i] - function(i, time)) > y_diff:
            y_diff = abs(y1_values[i] - function(i, time))
        if x1_values[i] < 0:
            square_norm += np.square(abs(function(i, time) - y1_values[i])) * h1
        else:
            square_norm += np.square(abs(function(i, time) - y1_values[i])) * h2

    max_norm = y_diff/max(y2_values)

    ax.cla()
    ax.plot(x1_values, y1_values, color='blue', label='Discret')
    #ax.plot(x2_values, y2_values, color='red', linestyle='--', label='Analytics')
    #ax.plot(x2_values, diff_values, color='green', label='Abs_Error') # график относительных ошибок
    #ax.text(0.30, 1.1, f'Max Norm: {max_norm:.4f}', fontsize=12, color='black')
    #ax.text(-1, 1.1, f'Square Norm: {square_norm:.4f}', fontsize=12, color='black')
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_xlabel('x')
    ax.set_ylabel('u')
    ax.grid(True)
    ax.set_xticks(np.arange(-1, 1.2, 0.2))
    ax.set_yticks(np.arange(-1, 1.2, 0.2))
    ax.legend()
    plt.draw()


fig, ax = plt.subplots()

plt.subplots_adjust(bottom=0.25)

time_slider_ax = plt.axes([0.25, 0.1, 0.65, 0.03])
time_slider = Slider(time_slider_ax, 'Time', valmin=min(times), valmax=max(times), valinit=times[0], valstep=times[1]-times[0])
time_slider.on_changed(update)

exec(open('graph1.py').read())

#plt.get_current_fig_manager().full_screen_toggle()
plt.show()