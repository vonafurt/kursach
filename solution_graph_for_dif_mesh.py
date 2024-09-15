import matplotlib.pyplot as plt
#from matplotlib.widgets import Slider
import math
import numpy as np
import pandas as pd
import csv


def plot_graphs(x_graph, y_graph):
    num_graphs = len(x_graph)
    for i in range(num_graphs):
        plt.plot(x_graph[i], y_graph[i], label=f'Graph {i+1}')

    plt.xlabel('X values')
    plt.ylabel('Y values')
    plt.title('Graphs')
    plt.legend()
    plt.show()


x_graph = []
y_graph = []
count = 0


with open('results.csv', newline='') as csvfile:
    # Создаем читатель CSV файла с разделителем ";"
    csv_reader = csv.reader(csvfile, delimiter=';')
    for row in csv_reader:
        row_array = row
        print(len(row_array))
        x_step = 2 / (len(row_array) - 1)
        x = []
        x_tmp = -1
        x.append(x_tmp)
        for i in range(len(row_array) - 1):
            x_tmp += x_step
            x.append(x_tmp)
        print(x)
        print(row_array)
        row_arr = [float(y_str) for y_str in row_array]
        x_graph.append(x)
        y_graph.append(row_arr)
        count += 1
        plt.plot(x, row_arr)

plt.legend(['5', '9', '17', '33', '65', '129', '257', '513', '1025'])
plt.grid(True)
plt.show()
#plot_graphs(x_graph, y_graph)

