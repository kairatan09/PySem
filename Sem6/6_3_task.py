# Дан список чисел. Посчитайте,
# сколько в нем пар элементов,
# равных друг другу.

# Считается, что любые два элемента,
# равные друг другу образуют одну пару,
# которую необходимо посчитать.
# Вводится список чисел.
# Все числа списка находятся на разных строках.

list_n = [int(input()) for i in range (int(input('Введите количество элементов списка n: ')))]
count = [list_n[i] for i in range(len(list_n)) for j in range(i + 1, len(list_n)) if list_n[j] == list_n[i]]
print(count, len(count))


# 2 вариант
# nums = input().split()
# print(sum(nums.count(x) - 1 for x in nums) // 2)