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
    if abs(x) < 0.0000001:
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
    count = 2
    while count < 5000:
        time_t = time.time()
        n1 = count
        n2 = count
        n = n1 + n2 + 1
        ro = 0.5
        func = [[0] * n for _ in range(2)]
        func1 = [[0] * n for _ in range(2)]
        tao = ro / (4 * max(k(-1) * n1 * n1, k(1) * n2 * n2))
        J = math.ceil(0.1 / tao)
        h1 = 1.0 / n1
        h2 = 1.0 / n2

        func[0][-1] = 0
        func1[0][-1] = 0
        func[0][0] = 0
        func1[0][0] = 0

        for i in range(1, n - 1):
            if i < n1:
                func[0][i] = math.sin((-1 + h1 * i) * math.pi)
            else:
                func[0][i] = math.sin((-1 + n1 * h1 + h2 * (i - n1)) * math.pi)


        delta1 = 0.0
        delta2 = 0.0
        delta0_p = 0.0
        delta0_m = 0.0
        alpha_p = - h2 / (h2)
        alpha_m = - h1 / (h1)


        for t in range(1, J):
            for i in range(n):
                if i == 0 or i == n - 1:
                    func[1][i] = 0
                else:
                    if i < n1:
                        func[1][i] = func[0][i] - tao * LhW(h1, h2, -1 + i * h1, func, i) + tao * f(t, -1 + i * h1)
                    else:
                        func[1][i] = func[0][i] - tao * LhW(h1, h2, -1 + n1 * h1 + (i - n1) * h2, func, i) + tao * f(t, -1 + n1 * h1 + (i - n1) * h2)

            for i in range(n):
                func[0][i] = func[1][i]

        delta1 = (func[0][n1 + 1] - func[0][n1]) / h2
        delta2 = (func[0][n1 + 2] - func[0][n1]) / (2 * h2)
        delta0_p = (1 - alpha_p) * delta1 + alpha_p * delta2
        delta1 = (func[0][n1] - func[0][n1 - 1]) / h1
        delta2 = (func[0][n1] - func[0][n1 - 2]) / (2 * h1)
        delta0_m = (1 - alpha_m) * delta1 + alpha_m * delta2
        F_p = k(1) * delta0_p
        F_m = k(-1) * delta0_m
        d = 2 * (F_p - F_m) / (abs(F_p) + abs(F_m))

        file1.write(str(n) + ";")
        file1.write(str(F_p) + ';')
        file1.write(str(F_m) + ';')
        file1.write(str(abs(F_p) - abs(F_m)) + ';')
        file1.write(str(d) + ';')
        file1.write("\n")
        print("time: ", time.time() - time_t, "mesh: ", 2 * count)
        count *= 2
    return time.time() - time_t


with open("results2.csv", "w") as file1:
    file1.write("n;F+;F-;F+-F-;d;\n")
    print(main())