'''
Большой подвиг 3. В виде строки записано арифметическое выражение, например:

"10 + 25 - 12"

или

"10 + 25 - 12 + 20 - 1 + 3"

и т. д. То есть, количество действий может быть разным.

Необходимо выполнить вычисление и результат отобразить на экране. Полагается, что в качестве арифметических операций здесь используется только сложение (+) и вычитание (-), а в качестве операндов - целые неотрицательные числа. Следует учесть, что эти операторы могут быть записаны как с пробелами, так и без них.

Sample Input:

10+25 - 12

Sample Output:

23
'''

# put your python code here
'''str = input().strip()
s = ''
s2 = ''
res = 0
for i in str:
    if i.isdigit():
        s = s + i
    else:
        for j in str[i+1:]:
            if j.isdigit():
                s2 = s2 + j
    if i == '+':
        res += (int(s)+int(s2))
    else:
        res += (int(s)-int(s2))
    i += len(s2)
    s = ''
    s2 = ''
print(res)'''
str = input()
str = str.replace(" ", "")
str = str.replace("+", " ")
str = str.replace("-", " -")
n = list(map(int, str.split()))
print(sum(n))