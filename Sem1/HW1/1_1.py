# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

n = int(input('Введите трехзначное число: '))
Sum = 0
if 99 < n < 1000:
    while n > 0:
        Sum += n % 10
        n = n // 10
    print(f"Сумма цифр трехзначного числа равно - {Sum}")
else:
    print("Введенное число не трехзначное")
