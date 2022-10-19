# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

# Пример двух заданных многочленов:
# 23x⁹ - 16x⁸ + 3x⁷ + 15x⁴ - 2x³ + x² + 20 = 0
# 17x⁹ + 15x⁸ - 8x⁷ + 15x⁶ - 10x⁴ + 7x³ - 13x¹ + 33 = 0

# Результат:
# 40x⁹ - x⁸ -5x⁷ + 15x⁶ +5x⁴ + 5x³ + x² - 13x¹ + 53 = 0



def power_zero(value):
    for i in value:
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

def x(value, d2):
    t = value.split('x')
    for i in range(1, 10):
        if t[1] == d2[i][1]:
            p = i
            break
            
    if t[0] == '+':
        arg = 1
    elif t[0] == '-':
        arg = -1
    else:
        arg = int(t[0])
    return arg, p

with open('Unicode.txt', 'r', encoding='utf-8') as U:
    d = U.readline()

#print(d)
d1 = d.split()
d2 = []
for i in range(len(d1)):
    d2.append(d1[i].split(':'))
#print(d2)

with open('polynomial_1.txt', 'r', encoding='utf-8') as f:
    polynomial_1 = f.readline()


polynomial_1 = delete_0(polynomial_1)
polynomial_1 = join_plus_minus(polynomial_1)
print(polynomial_1)
first_list = polynomial_1.split()

#print(first_list[-1])

result = [0]
for i in range(8):
    result.append(0)

if power_zero(first_list[-1]):
    result.append(int(first_list[-1]))
else:
    result.append(0)
#print(result)

for i in range(2, len(first_list)+1):
    a, b = x(first_list[-i], d2)
    result[-b-1] = a
print(result)

with open('polynomial_2.txt', 'r', encoding='utf-8') as f:
    polynomial_2 = f.readline()

polynomial_2 = delete_0(polynomial_2)
polynomial_2 = join_plus_minus(polynomial_2)
print(polynomial_2)
second_list = polynomial_2.split()

# second_result = [0]
# for i in range(8):
#     second_result.append(0)

if power_zero(second_list[-1]):
    result[-1] = result[-1] + int(second_list[-1])
    #second_result.append(int(second_list[-1]))
# else:
#     second_result.append(0)
#print(second_result)


for i in range(2, len(second_list)+1):
    a, b = x(second_list[-i], d2)
    result[-b-1] = result[-b-1] + a

print(result)