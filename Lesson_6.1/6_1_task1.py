'''
Подвиг 3. Вводятся данные в формате ключ=значение в одну строчку через пробел. Значениями здесь являются целые числа (см. пример ниже). Необходимо на их основе создать словарь d с помощью функции dict() и вывести его на экран командой:

print(*sorted(d.items()))

Sample Input:

one=1 two=2 three=3

Sample Output:

('one', 1) ('three', 3) ('two', 2)
'''

# put your python code here
str = input().replace("=",' ')
lst = list(str.split())
lst = [[lst[i], int(lst[i+1])] for i in range(0,len(lst) -1, 2) ]
#print(lst)
d = dict(lst)
print(*sorted(d.items()))
