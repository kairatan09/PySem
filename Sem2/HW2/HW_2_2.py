# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.


# s = int(input('Введите сумму чисел: '))
# р = int(input('Введите произведение чисел: '))

# x = (s + (s**2 - 4*p)**0,5)/2
# y = s - x

# print(x, y)


s = int(input())
p = int(input())
num_1 = 1

while num_1 < p:
    num_2 = s - num_1
    if s == num_1 + num_2 and p == num_2 * num_1:
        print(num_1, num_2)
        break
    num_1 += 1