# Задача №23. Решение в группах
# Дан массив, состоящий из целых чисел.
# Напишите программу, которая подсчитает количество элементов массива, больших предыдущего (элемента с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)

list_nums = [0, -1, 5, 2, 3]
print(sum([list_nums[i] > list_nums[i - 1] for i in range(1, len(list_nums))]))