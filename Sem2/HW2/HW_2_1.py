# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

coin = int(input('Введите количество монеток: '))
count_0 = 0
count_1 = 0
for i in range(coin):
    n = int(input(f"Введите значение монетки {i+1}: "))
    if n == 0:
        count_0 += 1
    else:
        count_1 += 1
if count_1 > count_0:
    print(f"Минимальное число монеток, которые нужно перевернуть равно - {count_0}")
else:
    print(f"Минимальное число монеток, которые нужно перевернуть равно - {count_1}")



# Сохранен для себя
# n = int(input())
# count = 0

# for i in range(n):
#     if int(input()):
#         count += 1

# print(min(count, n - count))