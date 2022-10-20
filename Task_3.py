# 3). Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.

from random import randint


n = int(input('Введите число элементов в списке: '))
lst_random = []
for i in range(n):
    lst_random.append(randint(0, 10))
print(f'Исходная последовательность: {lst_random}')

lst_new = []
for elem in lst_random:
    if lst_random.count(elem) < 2:
        lst_new.append(elem)
print(
    f'Список неповторяющихся элементов исходной последовательности: {lst_new}')
