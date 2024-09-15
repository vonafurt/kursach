from cx_Freeze import setup, Executable
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import math
import numpy as np
import pandas as pd

pathk = 'results1.csv'

df1 = pd.read_csv(pathk, sep=';', decimal=',')

times = list(df1['Time'])
u = df1.iloc[0:, 1].values.astype(float)
d = df1.iloc[0:, 2].values.astype(float)
F_p = df1.iloc[0:, 3].values.astype(float)
F_m = df1.iloc[0:, 4].values.astype(float)

times = [float(time_str) for time_str in times]
u = [float(time_str) for time_str in u]
d = [float(time_str) for time_str in d]
F_p = [float(time_str) for time_str in F_p]
F_m = [float(time_str) for time_str in F_m]

fig1, ax1 = plt.subplots(2, 3)

ax1[0, 0].grid(True)
ax1[0, 1].grid(True)
ax1[1, 0].grid(True)
ax1[1, 1].grid(True)
ax1[0, 0].plot(times, u, marker='o', linestyle='None', markersize=1, color='blue')
ax1[0, 0].set_xlabel('t')
ax1[0, 0].set_ylabel('u')
ax1[0, 1].plot(times, d, marker='o', linestyle='None', markersize=1, color='blue')
ax1[0, 1].set_xlabel('t')
ax1[0, 1].set_ylabel('d')
ax1[1, 0].plot(times, [-i for i in F_m], linestyle='-', markersize=1, color='blue')
ax1[1, 0].plot(times, F_p, linestyle='-', markersize=1, color='red')
ax1[1, 1].plot(times, F_m, linestyle='-', markersize=1, color='blue')
ax1[1, 1].plot(times, F_p, linestyle='-', markersize=1, color='red')
ax1[1, 1].legend(labels=['F-', 'F+'])
ax1[1, 0].set_xlabel('t')
ax1[1, 0].set_ylabel('F')
ax1[1, 1].set_xlabel('t')
ax1[1, 1].set_ylabel('F')
ax1[1, 2].axis('off')
ax1[0, 2].axis('off')
# print(list(df1['n1'])[0])
ax1[1, 2].text(0.30, 1.9, f"n1: {list(df1['n1'])[0] :.4f}", fontsize=12, color='black')
ax1[1, 2].text(0.30, 1.7, f"n2: {list(df1['n2'])[0] :.4f}", fontsize=12, color='black')
ax1[1, 2].text(0.30, 1.5, f"k-: {float(list(df1['k-'])[0]) :.4f}", fontsize=12, color='black')
ax1[1, 2].text(0.30, 1.3, f"k+: {float(list(df1['k+'])[0]) :.4f}", fontsize=12, color='black')
ax1[1, 2].text(0.30, 1.1, f"tao: {float(list(df1['tao'])[0]) :.12f}", fontsize=12, color='black')
ax1[1, 2].text(0.30, 0.9, f'u at moment T: {u[-1]:.4f}', fontsize=12, color='black')
ax1[1, 2].text(0.30, 0.7, f'd at moment T: {d[-1]:.4f}', fontsize=12, color='black')
ax1[1, 2].text(0.30, 0.5, f'F+ at moment T: {F_p[-1]:.4f}', fontsize=12, color='black')
ax1[1, 2].text(0.30, 0.3, f'F- at moment T: {F_m[-1]:.4f}', fontsize=12, color='black')
plt.show()
