# Задача №19. Решение в группах. Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K – положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]

list_nums = [1, 2, 3, 4, 5]
k = int(input('Введите число: '))
n = len(list_nums)

print(list_nums)

for i in range(0, k % n):
    list_nums.insert(0, list_nums.pop())

print(list_nums)


# def shift(list_nums, steps):
#     if steps < 0:
#         steps = abs(steps)
#         for i in range(steps):
#             list_nums.append(list_nums.pop(0))
#     else:
#         for i in range(steps):
#             list_nums.insert(0, list_nums.pop())

# nums = [1, 2, 3, 4, 5]
# shift(nums, 1)
# print(nums)