# Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от -100 до 100) многочлена и записать в файл многочлен степени k
# k - максимальная степень многочлена, следующий степень следующего на 1 меньше и так до ноля
# Коэффициенты расставляет random, поэтому при коэффициенте 0 просто пропускаем данную итерацию степени
# Пример:
# k=2 -> 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10x² = 0
# k=5 -> 3x⁵ + 5x⁴ - 6x³ - 3x = 0

def is_int(value):  # Проверка введенного значения на целое число
    try:
        int(value)
        return True
    except ValueError:
        return False

def find_power(value):  # Перевод любой степени в строку
    if len(str(value)) > 1:
        value = str(value)
        p = ''
        for i in range(len(value)):
            #x = value[i]
            p = p + str(chr(unicode[int(value[i])]))
    else:
        p = str(chr(unicode[value]))
    return p

k = input('Введите число k: ')

while not is_int(k) or int(k) < 2:  # Проверка условий для введенного значения
    if not is_int(k):
        print('Введено не целое число')
        k = input('Введите целое число k: ')
        continue
    elif int(k) < 2:
        print('Число не может быть отрицательным или равным 0 или равным 1')
        k = input('Введите целое положительное число больше нуля: ')

k1 = int(k)

        #   0     1    2    3     4    5     6     7      8     9
unicode = [8304, 185, 178, 179, 8308, 8309, 8310, 8311, 8312, 8313]

result = ''
import random
for i in range(k1, 0, -1):
    number = random.randint(-100, 100)
    p = find_power(i)
    if number == 0:
        continue
    elif number == 1:
        if i == k1:
            result = result + f'x{p} '
        else:
            result = result + f'+ x{p} '
    elif number > 1:
        if i == k1:
            result = result + f'{number}x{p} '
        else:
            result = result + f'+ {number}x{p} '
    elif number == -1:
        result = result + f'- x{p} '
    else:
        result = result + f'- {abs(number)}x{p} '

if str(chr(185)) in result:
    result = result[:-2] +' '
   
number = random.randint(-100, 100)
if number == 0:
    result = result + '= 0'
elif number > 0:
    result = result + f'+ {number} = 0'
else:
    result = result + f'- {abs(number)} = 0'

print(result)

with open('Task_4.txt', 'a', encoding='utf-8') as f:
    f.write(result + '\n')

