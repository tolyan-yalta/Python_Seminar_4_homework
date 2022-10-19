# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

# Пример двух заданных многочленов:
# 23x⁹ - 16x⁸ + 3x⁷ + 15x⁴ - 2x³ + x² + 20 = 0
# 17x⁹ + 15x⁸ - 8x⁷ + 15x⁶ - 10x⁴ + 7x³ - 13x¹ + 33 = 0

# Результат:
# 40x⁹ - x⁸ -5x⁷ + 15x⁶ +5x⁴ + 5x³ + x² - 13x¹ + 53 = 0


def power_zero(value):  # Проверка на наличие элемента без 'x'
    for i in value:
        k = ord(i)
        if ord(i) == 120:
            return False
        elif i == value[-1]:
            return True

def delete_0(value):    # Удаление '= 0'
    value = value[:-1].rstrip()
    value = value.replace('=', ' ').rstrip()
    return value

def join_plus_minus(value):   # Удаление лишних пробелов между +/- и значением
    count_plus = value.count('+ ')
    while count_plus != 0:
        count_plus = value.count('+ ')
        value = value.replace('+ ', '+')
    count_minus = value.count('- ')
    while count_minus != 0:
        count_minus = value.count('- ')
        value = value.replace('- ', '-')
    return value

def change_code_94(value):   # Замена ^
    count_code = value.count('^')
    for i in range(count_code):
        temp = value.find('^')
        value = value[:temp] + chr(Unicode[int(value[temp+1:temp+2])]) + value[temp+2:]
    return value

def change_code_42(value):   # Замена *
    count_code = value.count('**')
    for i in range(count_code):
        temp = value.find('**')
        value = value[:temp] + chr(Unicode[int(value[temp+2:temp+3])]) + value[temp+3:]
    return value

def return_number_and_power(value): # Возвращает из строки число и степень
    t0, t1 = value.split('x')
    for i in range(1, 10):
        if ord(t1) == Unicode[i]:
            power = i
            break
            
    if t0 == '+':
        number = 1
    elif t0 == '-':
        number = -1
    else:
        number = float(t0)
    return number, power

        #   0     1    2    3     4    5     6     7      8     9    ^  * 
Unicode = [8304, 185, 178, 179, 8308, 8309, 8310, 8311, 8312, 8313, 94, 42]

with open('polynomial_1.txt', 'r', encoding='utf-8') as f:
    polynomial_1 = f.readline()

print(polynomial_1)
polynomial_1 = delete_0(polynomial_1)
polynomial_1 = join_plus_minus(polynomial_1)
polynomial_1 = change_code_94(polynomial_1)
polynomial_1 = change_code_42(polynomial_1)

first_list = polynomial_1.split()

result = [0]
for i in range(9):
    result.append(0)

if power_zero(first_list[-1]):
    result[-1] = float(first_list[-1])

for i in range(2, len(first_list)+1):
    number, power = return_number_and_power(first_list[-i])
    result[-power-1] = number

with open('polynomial_2.txt', 'r', encoding='utf-8') as f:
    polynomial_2 = f.readline()

print(polynomial_2)
polynomial_2 = delete_0(polynomial_2)
polynomial_2 = join_plus_minus(polynomial_2)
polynomial_2 = change_code_94(polynomial_2)
polynomial_2 = change_code_42(polynomial_2)

second_list = polynomial_2.split()

if power_zero(second_list[-1]):
    result[-1] = result[-1] + float(second_list[-1])

for i in range(2, len(second_list)+1):
    number, power = return_number_and_power(second_list[-i])
    result[-power-1] = result[-power-1] + number

polynomial_result = ''
for i in range(9):
    if round(result[i]) - int(result[i]) == 0:
        result[i] = int(result[i])
    if result[i] == 0:
        continue
    elif result[i] == 1:
        if i == 0:
            polynomial_result = polynomial_result + 'x' + str(chr(Unicode[9-i])) + ' '
        else:
            polynomial_result = polynomial_result + '+ ' + 'x' + str(chr(Unicode[9-i])) + ' '
    elif result[i] == -1:
        polynomial_result = polynomial_result + '- ' + 'x' + str(chr(Unicode[9-i])) + ' '
    elif result[i] > 0:
        if i == 0:
            polynomial_result = polynomial_result + str(result[i]) + 'x' + str(chr(Unicode[9-i])) + ' '
        else:
            polynomial_result = polynomial_result + '+ ' + str(result[i]) + 'x' + str(chr(Unicode[9-i])) + ' '
    elif result[i] < -1:
        polynomial_result = polynomial_result + '- ' + str(abs(result[i])) + 'x' + str(chr(Unicode[9-i])) + ' '
if round(result[9]) - int(result[9]) == 0:
        result[9] = int(result[9])
if result[9] > 0:
    polynomial_result = polynomial_result + '+ ' + str(result[9]) + ' = 0'
elif result[9] < 0:
    polynomial_result = polynomial_result + '- ' + str(abs(result[9])) + ' = 0'
else:
    polynomial_result = polynomial_result + ' = 0'
print(polynomial_result)

with open('polynomial_result.txt', 'a', encoding='utf-8') as f:
    f.write(polynomial_result + '\n')
