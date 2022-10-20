# Задайте последовательность цифр. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.
# Пример:
# 47756688399943 -> [5]
# 1113384455229 -> [8,9]
# 1115566773322 -> []

def is_int(value):  # Проверка введенного значения на целое число
    try:
        int(value)
        return True
    except ValueError:
        return False

length = input('Введите длину последовательности цифр: ')

while not is_int(length) or int(length) < 1 or int(length) == 1:  # Проверка условий для введенного значения
    if not is_int(length):
        print('Введено не целое число')
        length = input('Введите целое число: ')
        continue
    elif int(length) < 1:
        print('Длина последовательности не может быть отрицательной или равной 0')
        length = input('Введите целое положительное число больше единицы: ')
    elif int(length) == 1:
        print('Длина последовательности не может быть равна 1, нет смысла в задаче')
        length = input('Введите целое положительное число больше единицы: ')

import random
string_number = ''
for i in range(int(length)):
    string_number = string_number + str(random.randint(0, 10))

print(string_number)

i = 0
while i < len(string_number):
    if string_number.count(string_number[i]) > 1:
        string_number = string_number.replace(string_number[i], '')
        continue
    i += 1

list_result = []
for i in range(len(string_number)):
    list_result.append(int(string_number[i]))

print(list_result)