# 5). Даны два файла, в каждом из которых находится запись многочлена, приравненного к нулю.
# Задача - сформировать файл, содержащий сумму многочленов (суммируем подобные слагаемые).
# Пример:
# 1 Файл : 2*x2 + 4*x + 5 = 0
# 2 Файл : 4*x2 + 7*x + 9 = 0
# 3 Файл: (содержит результат) 6*x2 + 11*x + 14 = 0
# Пример:
# 1 Файл : 2*x3 + 4*x2 + 5*x + 1 = 0
# 2 Файл : 4*x2 + 7*x + 9 = 0
# 3 Файл: (содержит результат) 2*x3 + 8*x2 + 12


from random import randint

for i in range(1, 3):
    with open(f'text_{i}.txt', 'w') as file:
        result = ''
        n = randint(1, 4)
        if n == 1:
            file.write(f'{randint(0, 101)}*x +{randint(0, 101)} = 0')
        else:
            while n != 0 and n > 1:
                result += f'{randint(0, 101)}*x{n} + '
                n -= 1
            else:
                result += f'{randint(0, 101)}*x + '
            file.write(f'{result}{randint(0, 101)} = 0')

file1 = 'text_1.txt'
file2 = 'text_2.txt'


def extraction_koef(file):
    with open(str(file), 'r') as f:
        koef_list = f.read().replace('*x', ' ') \
            .replace(' +', '') \
            .replace('  ', ' ') \
            .replace(' = 0', '') \
            .split()
        for i in range(len(koef_list), 2, -2):
            if len(koef_list) == i:
                for k in range(1, int(i/2)):
                    del koef_list[k]
                break
        koef_list = list(map(int, koef_list))
        return koef_list


list1 = extraction_koef(file1)
list2 = extraction_koef(file2)
print(list1)
print(list2)

result = ''
if len(list1) < len(list2):
    list1, list2 = list2, list1
j = len(list1) - len(list2)
degree = len(list1) - 1
i = 0
while j != 0:
    result += f'{list1[i]}*x{degree} + '
    j -= 1
    i += 1
    degree -= 1
while i < len(list1):
    if degree == 1:
        result += f'{list1[i] + list2[i - (len(list1) - len(list2))]}*x + {list1[i+1] + list2[(i+1) - (len(list1) - len(list2))]} = 0'
        break
    result += f'{list1[i] + list2[i - (len(list1) - len(list2))]}*x{degree} + '
    i += 1
    degree -= 1

print(result)

with open('text_3.txt', 'w') as f:
    f.write(result)
