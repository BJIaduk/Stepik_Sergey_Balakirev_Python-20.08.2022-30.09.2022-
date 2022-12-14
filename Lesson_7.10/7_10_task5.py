'''
Подвиг 5. Используя замыкания функций, объявите внутреннюю функцию, которая преобразует строку из списка целых чисел, записанных через пробел, либо в список, либо в кортеж. Тип коллекции определяется параметром tp внешней функции. Если tp = 'list', то используется список, иначе (при другом значении) - кортеж.

Далее, на вход программы поступают две строки: первая - это значение для параметра tp; вторая - список целых чисел, записанных через пробел. С помощью реализованного замыкания преобразовать эти данные в соответствующую коллекцию. Результат вывести на экран командой (lst - ссылка на коллекцию):

print(lst)

Sample Input:

list
-5 6 8 11 0 111 -456 3
Sample Output:

[-5, 6, 8, 11, 0, 111, -456, 3]
'''

# put your python code here
def func1(tips = "list"):
    def func2(s):
        nonlocal tips
        if tips == "list":
            return list(map(int,s.split()))
        else:
            return tuple(map(int,s.split()))
    return func2
st = input()
tip = input()
cnt = func1(st)
print(cnt(tip))
