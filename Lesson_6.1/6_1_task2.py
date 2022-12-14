'''
Подвиг 4. На вход программы поступают данные в виде набора строк в формате: 

ключ1=значение1
ключ2=значение2
...
ключN=значениеN

Ключами здесь выступают целые числа (см. пример ниже). Необходимо их преобразовать в словарь d (без использования функции dict()) и вывести его на экран командой:

print(*sorted(d.items()))

P. S. Для считывания списка целиком в программе уже записаны начальные строчки.

Sample Input:

5=отлично
4=хорошо
3=удовлетворительно

Sample Output:

(3, 'удовлетворительно') (4, 'хорошо') (5, 'отлично')
'''

import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список lst_in)
#print(lst_in)
lst_in = [list(lst_in[i].replace("=", ' ').split()) for i in range(len(lst_in))]
#print(lst_in)
lst_in = [ [ int(lst_in[i][0]),  lst_in[i][1]] for i in range(len(lst_in)) ]
#print(lst_in)
d = dict(lst_in)
print(*sorted(d.items()))
