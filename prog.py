import math
import time


def k(x):
    if x >= 0:
        return 1
    else:
        return 2


def f(t, x):
    return 0


def LhW(h1, h2, x, func, n):
    if abs(x) < 0.00000001:
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
    n1, n2 = map(int, input("Enter the number of nodes on the 1st and 2nd segment: ").split())
    time_t = time.time()

    n = n1 + n2 + 1
    ro = 0.5
    func = [[0] * n for _ in range(2)]
    func1 = [[0] * n for _ in range(2)]
    tao = ro / (4 * max(k(-1) * n1 * n1, k(1) * n2 * n2))
    #tao = 10 ** (-5)
    J = math.ceil(float(input("How many seconds: ")) / tao)
    h1 = 1.0 / n1
    h2 = 1.0 / n2

    func[0][-1] = 1
    func1[0][-1] = 1
    func[0][0] = 0
    func1[0][0] = 0

    for i in range(1, n - 1):
        if i < n1:
            func[0][i] = math.sin((-1 + h1 * i) * math.pi)
            #func[0][i] = -1
        else:
            func[0][i] = math.sin((-1 + n1 * h1 + h2 * (i - n1)) * math.pi)
            #func[0][i] = 1

    with open("results.csv", "w") as file:
        file.write("Time")
        for i in range(n):
            file.write(";")
            if i < n1:
                file.write(str(-1 + h1 * i))
            else:
                file.write(str(h2 * (i - n1)))
        file.write("\n")
        file.write("0,0")
        for i in range(n):
            file.write(";" + str(func[0][i]))
        file.write("\n")

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
            file.write(str(t * tao) + ";")
            for i in range(n):
                if i == 0:
                    func[1][i] = 0
                elif i == n - 1:
                    func[1][i] = 1
                else:
                    if i < n1:
                        func[1][i] = func[0][i] - tao * LhW(h1, h2, -1 + i * h1, func, i) + tao * f(t, -1 + i * h1)
                    else:
                        func[1][i] = func[0][i] - tao * LhW(h1, h2, -1 + n1 * h1 + (i - n1) * h2, func, i) + tao * f(t, -1 + n1 * h1 + (i - n1) * h2)
                file.write(str(func[1][i]))
                if i != n - 1:
                    file.write(";")
            file.write("\n")

            U[t - 1] = func[0][n1]

            delta1 = (func[0][n1 + 1] - func[0][n1]) / h2
            delta2 = (func[0][n1 + 2] - func[0][n1]) / (2 * h2)
            delta0_p = (1 - alpha_p) * delta1 + alpha_p * delta2
            delta1 = (func[0][n1] - func[0][n1 - 1]) / h1
            delta2 = (func[0][n1] - func[0][n1 - 2]) / (2 * h1)
            #delta1 = (func[0][n1 - 1] - func[0][n1]) / h1
            #delta2 = (func[0][n1 - 2] - func[0][n1]) / (2 * h1)
            delta0_m = (1 - alpha_m) * delta1 + alpha_m * delta2
            F_p[t - 1] = k(1) * delta0_p
            F_m[t - 1] = k(-1) * delta0_m
            d[t - 1] = 2 * (F_p[t - 1] - F_m[t - 1]) / (abs(F_p[t - 1]) + abs(F_m[t - 1]))

            #F_p[t - 1] = k(1) * (func[0][n1 + 1] - func[0][n1]) / h2
            #F_m[t - 1] = k(-1) * (func[0][n1] - func[0][n1 - 1]) / h1

            for i in range(n):
                func[0][i] = func[1][i]

        U[J - 1] = func[0][n1]

        delta1 = (func[0][n1 + 1] - func[0][n1]) / h2
        delta2 = (func[0][n1 + 2] - func[0][n1]) / (2 * h2)
        delta0_p = (1 - alpha_p) * delta1 + alpha_p * delta2
        delta1 = (func[0][n1] - func[0][n1 - 1]) / h1
        delta2 = (func[0][n1] - func[0][n1 - 2]) / (2 * h1)
        #delta1 = (func[0][n1 - 1] - func[0][n1]) / h1
        #delta2 = (func[0][n1 - 2] - func[0][n1]) / (2 * h1)
        delta0_m = (1 - alpha_m) * delta1 + alpha_m * delta2
        F_p[J - 1] = k(1) * delta0_p
        F_m[J - 1] = k(-1) * delta0_m
        d[J - 1] = 2 * (F_p[J - 1] - F_m[J - 1]) / (abs(F_p[J - 1]) + abs(F_m[J - 1]))

        #F_p[J - 1] = k(1) * (func[0][n1 + 1] - func[0][n1]) / h2
        #F_m[J - 1] = k(-1) * (func[0][n1] - func[0][n1 - 1]) / h1

    with open("results1.csv", "w") as file1:
        file1.write("Time;u;d;F+;F-;n1;n2;k-;k+;tao\n")
        flag = False
        for t in range(J):
            file1.write(str(t * tao) + ";")
            file1.write(str(U[t]) + ';')
            file1.write(str(d[t]) + ';')
            file1.write(str(F_p[t]) + ';')
            file1.write(str(F_m[t]))
            if not flag:
                file1.write(';' + str(n1) + ';' + str(n2) + ';' + str(k(-1)) + ';' + str(k(1)) + ';' + str(tao))
                flag = True
            file1.write("\n")
    return time.time() - time_t


print(main())

