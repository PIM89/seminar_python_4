# 1). Вычислить число π c заданной точностью d
# Пример:
# при d = 0.001, π = 3.141 10^(-1)≤d≤10^(-10)


# import math

# d = int(input('Введите количество знаков после запятой у числа Пи: '))
# print(str(math.pi)[:d+2])

d = int(input('Введите количество знаков после запятой у числа Пи: '))
accuracy = 1
for i in range(d):
    accuracy /= 10
print(f'Заданная точность: d = {accuracy}')
k = 1
pi = 0
for i in range(1000000):
    if i % 2 == 0:
        pi += 4 / k
    else:
        pi -= 4 / k
    k += 2
print(str(pi)[:d+2])
