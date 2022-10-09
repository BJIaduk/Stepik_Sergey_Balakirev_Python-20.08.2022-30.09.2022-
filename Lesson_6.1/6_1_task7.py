'''
Подвиг 9. Пользователь вводит в цикле целые положительные числа, пока не введет число 0. 
Для каждого числа вычисляется квадратный корень (с точностью до сотых) и значение выводится 
на экран (в столбик). С помощью словаря выполните кэширование данных так, чтобы при повторном 
вводе того же самого числа результат не вычислялся, а бралось ранее вычисленное значение из словаря. 
При этом на экране должно выводиться:

значение из кэша: <число>

Sample Input:

1
2
3
3
2
4
0
Sample Output:

1.0
1.41
1.73
значение из кэша: 1.73
значение из кэша: 1.41
2.0
'''

# put your python code here
import math
d = {}
a = int(input())
while a != 0:
    flag = True
    if a not in d:
        flag = False
        d[a] = round(math.sqrt(a), 2)
        print(round(math.sqrt(a), 2))
    else:
        print(f"значение из кэша: {d[a]}")
    a = int(input())
