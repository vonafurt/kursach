import math
import pandas as pd
import decimal

df = pd.read_csv('results1.csv', delimiter=';')

last_three_rows = df.tail(3)
h = 1 / (last_three_rows.iloc[2, 0] - 1)
print('h ', h)
f1p = last_three_rows.iloc[2, 1]
f2p = last_three_rows.iloc[1, 1]
f3p = last_three_rows.iloc[0, 1]
f1m = last_three_rows.iloc[2, 2]
f2m = last_three_rows.iloc[1, 2]
f3m = last_three_rows.iloc[0, 2]
u1 = last_three_rows.iloc[2, 3]
u2 = last_three_rows.iloc[1, 3]
u3 = last_three_rows.iloc[0, 3]
print(f1p, f2p, f3p)

alpha_fp = math.log2((f3p - f2p) / (f2p - f1p))
alpha_fm = math.log2((f3m - f2m) / (f2m - f1m))
alpha_u = math.log2((u3 - u2) / (u2 - u1))

f0p = f2p / (1 - 2 ** alpha_fp)
cfp = (f1p - f0p) / h ** alpha_fp

f0m = f2m / (1 - 2 ** alpha_fm)
cfm = (f1m - f0m) / h ** alpha_fm

u0 = u2 / (1 - 2 ** alpha_u)
cu = (u1 - u0) / h ** alpha_u


print("alpha_F_p", alpha_fp)
print("alpha_F_m", alpha_fm)
print("alpha_u", alpha_u)
print("C F_p ", cfp)
print("C F_m ", cfm)
print("C u ", cu)
print("F0 F_p ", f0p)
print("F0 F_m ", f0m)
print("F0 u ", u0)


F3 = last_three_rows.iloc[0, 1] - last_three_rows.iloc[0, 2]
F2 = last_three_rows.iloc[1, 1] - last_three_rows.iloc[1, 2]
F1 = last_three_rows.iloc[2, 1] - last_three_rows.iloc[2, 2]
alpha = math.log2((F3 - F2)/(F2 - F1))
print("F_p - F_m alpha", math.log2((F3 - F2)/(F2 - F1)))
f0 = F2 / (1 - 2 ** alpha)
c = (F1 - f0) / h ** alpha
print("F_p - F_m C ", c)
print("F_p - F_m F0 ", f0)