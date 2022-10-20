# 2) Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

num = int(input("Введите число: "))
i = 2
list_numbers = []
while i <= num:
    if num % i == 0:
        list_numbers.append(i)
        num = num // i
        i = 2
    else:
        i += 1
print(f"Список простых множителей числа: {list_numbers}")
