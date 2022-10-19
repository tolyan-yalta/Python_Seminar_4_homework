# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def simple_number(number):  # Проверка простое ли число
    if number == 1 or number == 2 or number  == 3:
        return True
    if number % 2 == 0:
        return False
    i = 3
    while i**2 < number:
        if number % i == 0:
            return False
        i += 2 
    return True

def is_int(value):  # Проверка введенного значения на целое число
    try:
        int(value)
        return True
    except ValueError:
        return False

# N = 2821      # 1, 7, 13, 31
N = input('Введите число N: ')

while not is_int(N) or int(N) < 1:  # Проверка условий для введенного значения
    if not is_int(N):
        print('Введено не целое число')
        N = input('Введите целое число N: ')
        continue
    elif int(N) < 1:
        print('Число не может быть отрицательным или равным 0')
        N = input('Введите целое положительное число больше нуля: ')

N = int(N)

list_simple_number = []
for i in range(1, N + 1):
    if N % i == 0 and simple_number(i):
        list_simple_number.append(i)

print(f'Для введеннного числа список простых множителей будет: {list_simple_number}')
