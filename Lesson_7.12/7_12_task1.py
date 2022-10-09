'''
Подвиг 1. Вводится строка целых чисел через пробел. Напишите функцию, которая преобразовывает эту строку в список чисел и возвращает их сумму.

Определите декоратор для этой функции, который имеет один параметр start - начальное значение суммы.
Примените декоратор со значением start=5 к функции и вызовите декорированную функцию для введенной строки s:

s = input()

Результат отобразите на экране.

Sample Input:

5 6 3 6 -4 6 -1
Sample Output:

26
'''

# put your python code here
s = input()
def df_decor(start):
    def decor(func):
        def wrapper(*args, **kwargs):
            return start + func(*args)
        return wrapper
    return decor

@df_decor(start = 5)
def str_to_lst(s):
    s = list(map(int, s.split()))
    return sum(s)

x = str_to_lst(s)
print(x)
