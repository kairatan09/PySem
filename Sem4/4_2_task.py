# Задача №27. Решение в группах
# Пользователь вводит текст(строка). Словом считается последовательность непробельных символов идущих подряд, 
# слова разделены одним или большим числом пробелов. Определите, сколько различных слов содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea shore shells
# Output: 13

'''
She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells
'''

# text = input('Введите текст: ').upper()
# print(f'Количество различных слов в тексте: ', len(set(text.split())))

print('Количество различных слов в тексте: ', len(set(input('Введите текст: ').upper().split())))