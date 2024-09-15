import math
import time


def k(x):
    if x >= 0:
        return 1
    else:
        return 8


def f(t, x):
    return 0


def LhW(h1, h2, x, func, n):
    if abs(x) == 0:
        current_step = h2
        inv_step = h1
    elif x < 0:
        current_step = h1
        inv_step = h1
    else:
        current_step = h2
        inv_step = h2

    a = 2 / (current_step + inv_step)
    k1 = k(x + current_step / 2)
    k2 = k(x - inv_step / 2)
    u1 = (func[0][n + 1] - func[0][n]) / current_step
    u2 = (func[0][n] - func[0][n - 1]) / inv_step
    return -a * (k1 * u1 - k2 * u2)


def main():
    #n1, n2 = map(int, input("Enter the number of nodes on the 1st and 2nd segment: ").split())
    n1 = count
    n2 = count
    time_t = time.time()

    n = n1 + n2 + 1
    ro = 0.5
    func = [[0] * n for _ in range(2)]
    func1 = [[0] * n for _ in range(2)]
    tao = ro / (4 * max(k(-1) * n1 * n1, k(1) * n2 * n2))
    J = math.ceil(0.1 / tao)
    h1 = 1.0 / n1
    h2 = 1.0 / n2

    func[0][-1] = 1
    func1[0][-1] = 1
    #func[0][-1] = 0
    #func1[0][-1] = 0

    func[0][0] = 0
    func1[0][0] = 0

    for i in range(1, n - 1):
        if i < n1:
            func[0][i] = math.sin((-1 + h1 * i) * math.pi)
            #func[0][i] = -1
        else:
            func[0][i] = math.sin((-1 + n1 * h1 + h2 * (i - n1)) * math.pi)
            #func[0][i] = 1

    delta1 = 0.0
    delta2 = 0.0
    delta0_p = 0.0
    delta0_m = 0.0
    alpha_p = - h2 / h2
    alpha_m = - h1 / h1
    F_p = [0] * J
    F_m = [0] * J
    d = [0] * J
    U = [0] * J

    for t in range(1, J):
        for i in range(n):
            if i == 0:
                func[1][i] = 0
            elif i == n - 1:
                func[1][i] = 1
                #func[1][i] = 0
            else:
                if i < n1:
                    func[1][i] = func[0][i] - tao * LhW(h1, h2, -1 + i * h1, func, i) + tao * f(t, -1 + i * h1)
                else:
                    func[1][i] = func[0][i] - tao * LhW(h1, h2, -1 + n1 * h1 + (i - n1) * h2, func, i) + tao * f(t, -1 + n1 * h1 + (i - n1) * h2)
        U[t - 1] = func[0][n1]

        if mode != 1:
            #тепловые потоки по трем узлам
            delta1 = (func[0][n1 + 1] - func[0][n1]) / h2
            delta2 = (func[0][n1 + 2] - func[0][n1]) / (2 * h2)
            delta0_p = (1 - alpha_p) * delta1 + alpha_p * delta2
            delta1 = (func[0][n1] - func[0][n1 - 1]) / h1
            delta2 = (func[0][n1] - func[0][n1 - 2]) / (2 * h1)
            delta0_m = (1 - alpha_m) * delta1 + alpha_m * delta2
            F_p[t - 1] = k(1) * delta0_p
            F_m[t - 1] = k(-1) * delta0_m
            d[t - 1] = 2 * (F_p[t - 1] - F_m[t - 1]) / (abs(F_p[t - 1]) + abs(F_m[t - 1]))

        if mode == 1:
            #тепловые потоки по двум узлам

            F_p[t - 1] = k(1) * (func[0][n1 + 1] - func[0][n1]) / h2
            F_m[t - 1] = k(-1) * (func[0][n1] - func[0][n1 - 1]) / h1


        for i in range(n):
            func[0][i] = func[1][i]

    U[J - 1] = func[0][n1]

    if mode != 1:
        #тепловые потоки по трем узлам
        delta1 = (func[0][n1 + 1] - func[0][n1]) / h2
        delta2 = (func[0][n1 + 2] - func[0][n1]) / (2 * h2)
        delta0_p = (1 - alpha_p) * delta1 + alpha_p * delta2
        delta1 = (func[0][n1] - func[0][n1 - 1]) / h1
        delta2 = (func[0][n1] - func[0][n1 - 2]) / (2 * h1)
        delta0_m = (1 - alpha_m) * delta1 + alpha_m * delta2
        F_p[J - 1] = k(1) * delta0_p
        F_m[J - 1] = k(-1) * delta0_m
        d[J - 1] = 2 * (F_p[J - 1] - F_m[J - 1]) / (abs(F_p[J - 1]) + abs(F_m[J - 1]))

    if mode == 1:
        # тепловые потоки по двум узлам
        F_p[J - 1] = k(1) * (func[0][n1 + 1] - func[0][n1]) / h2
        F_m[J - 1] = k(-1) * (func[0][n1] - func[0][n1 - 1]) / h1

    for i in range(n):
        if i + 1 != n:
            file.write(str(func[1][i]) + ";")
        else:
            file.write(str(func[1][i]) + "\n")
    if mode1 == 0:
        # для вывода и рисования графиков на всех сетках
        for t in range(J):
            if t + 1 != J:
                file1.write(str(F_p[t]) + ';')
            else:
                file1.write(str(F_p[t]) + "\n")

        for t in range(J):
            if t + 1 != J:
                file1.write(str(F_m[t]) + ';')
            else:
                file1.write(str(F_m[t]) + "\n")

    if mode1 == 1:
        file1.write(str(n1 + n2 + 1) + ';' + str(F_p[-1]) + ';' + str(F_m[-1]) + ';' + str(func[1][n1]) + "\n")

    return time.time() - time_t


mode = input("approx for 3 points: 0, for 2 points: 1 ")
mode = int(mode)
mode1 = input("all results: 0, Runge: 1 ")
mode1 = int(mode1)
count = 2
with open("results.csv", "w") as file:
    with open("results1.csv", "w") as file1:
        if mode1 == 1:
            file1.write("n" + ';' + "F_p" + ';' + "F_m" + ';' + "u_0" + "\n")
        while count < 257:
            filename = f"results.csv"
            filename1 = f"results1.csv"
            print(main())
            count *= 2

