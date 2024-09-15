import matplotlib.pyplot as plt
import csv


x_graph = []
y_graph = []
count = 0
a = int(input("if F+ then 0, if F- then 1, if all then -1 "))

with open('results1.csv', newline='') as csvfile:
    # Создаем читатель CSV файла с разделителем ";"
    csv_reader = csv.reader(csvfile, delimiter=';')
    for row in csv_reader:
        if a == -1:
            row_array = row
            # print(len(row_array))
            x_step = 0.1 / (len(row_array) - 1)
            x = []
            x_tmp = 0
            x.append(x_tmp)
            for i in range(len(row_array) - 1):
                x_tmp += x_step
                x.append(x_tmp)
            # print(x)
            # print(row_array)
            row_arr = [float(y_str) for y_str in row_array]
            x_graph.append(x)
            y_graph.append(row_arr)
            count += 1
            plt.plot(x, row_arr)
        else:
            if a % 2 == 0:
                row_array = row
                #print(len(row_array))
                x_step = 0.1 / (len(row_array) - 1)
                x = []
                x_tmp = 0
                x.append(x_tmp)
                for i in range(len(row_array) - 1):
                    x_tmp += x_step
                    x.append(x_tmp)
                #print(x)
                #print(row_array)
                row_arr = [float(y_str) for y_str in row_array]
                x_graph.append(x)
                y_graph.append(row_arr)
                count += 1
                plt.plot(x, row_arr)
            a += 1

plt.xlabel('t')  # Подпись оси X
plt.ylabel('F')
if a == -1:
    plt.legend(['5', '5', '9', '9', '17', '17', '33', '33', '65', '65', '129', '129', '257', '257', '513', '513', '1025', '1025'])
else:
    plt.legend([str(2 ** i + 1) for i in range(2, count + 2)])
plt.grid(True)
plt.show()
#plot_graphs(x_graph, y_graph)

