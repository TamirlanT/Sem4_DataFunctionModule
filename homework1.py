# Вычислить число π c заданной точностью d
# Пример:
# - при d = 0.001, π = 3.141    10^{-1} ≤ d ≤10^{-10}

import math
d = int(input('Введите количесвто цифр после запятой --> '))
print (f'{math.pi:.{d}f}')