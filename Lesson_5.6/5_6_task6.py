'''
Большой подвиг 6. Вводится список целых чисел в одну строку через пробел. 
Необходимо выполнить его сортировку выбором по возрастанию (неубыванию). 
Идея алгоритма очень проста и проиллюстрирована на рисунке ниже.
'''

# put your python code here
lst = list(map(int, input().split()))
for i in range(len(lst)):
    min = lst[i]
    min_j = i
    for j in range(i, len(lst)):
        if lst[j] < min:
            min = lst[j]
            min_j = j
    lst[i], lst[min_j] = lst[min_j], lst[i]
print(*lst)
