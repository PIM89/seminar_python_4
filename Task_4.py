# 4). Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k и приравняйте его к нулю.
# Пример:
# k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# 2*x*2 + 4*x + 5 = 0
# или
# 2*x^2 + 4*x + 5 = 0

from random import randint
import random

k = int(input('Введите натуральную степень k: '))
while k <= 0:
    k = int(input('Введены не корректные данные! Введите натуральную степень k: '))

result = [0 for i in range(k)]
koef = random.sample(range(0, 101), k + 1)
print(f'Рандомные коэффициенты: {koef}')
for i in range(len(result)):
    result[i] = f'{koef[i]}x^{k}'
    k -= 1
result.append(str(koef[-1]))
print(f'До обработки: {result}')
for elem in result:
    if elem == 0:
        result.remove(elem)
    try:
        ind_x = elem.find('x')
        d = int(elem[:ind_x])
    except AttributeError:
        continue
    if d == 0 or elem == '0':
        result.remove(elem)
    if '^1' in elem:
        result.remove(elem)
        result.insert(-1, elem[:elem.find('^1')])
print(f'После обработки: {result}')
polynom = ''
for i in range(len(result) - 1):
    polynom += f'{result[i]} + '
polynom += f'{result[-1]} = 0'
print(polynom)

with open('text.txt', 'w') as f:
    f.write(polynom)
