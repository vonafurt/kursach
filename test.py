import math

# Значения функции при различных шагах
f1p = 1.0473418855722427
f2p = 1.046187458739206
f3p = 1.0459132998036544

# Вычисление разностей
delta_f21 = f2p - f1p
delta_f32 = f3p - f2p

# Проверка на деление на ноль
if delta_f21 == 0:
    raise ValueError("Разность f2p - f1p равна нулю, невозможно вычислить порядок точности")

# Вычисление порядка точности (alpha_fp)
alpha_fp = math.log2(delta_f32 / delta_f21)

# Вычисление истинного значения f0p и константы cfp
f0p = f2p - delta_f21 / (2 ** alpha_fp - 1)
cfp = (f1p - f0p) / (1/128) ** alpha_fp  # Используем значение шага h1

print("alpha_F_p:", alpha_fp)
print("C F_p:", cfp)
print("F0 F_p:", f0p)
