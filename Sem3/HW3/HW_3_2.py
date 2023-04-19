# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
# 1 2 3 4 5
# 6
# -> 5


import random

list_nums = [random.randint(1, 100) for i in range(int(input('Введите количество элементов списка: ')))]
x = int(input('Введите число Х: '))

print(list_nums)

min = abs(list_nums[0] - x)
minIndex = 0

for j in range(1, len(list_nums)):
    tmp = abs(list_nums[j] - x)
    if tmp < min:
        min = tmp
        minIndex = j

print(f'Число {list_nums[minIndex]} в списке самый близкий по величине элемент к числу {x}')