'''
Большой подвиг 7. Вводится список целых чисел в одну строку через пробел. 
Необходимо выполнить его сортировку по возрастанию (неубыванию) методом всплывающего пузырька. 
Идея алгоритма проста и показана на рисунке ниже.
'''

# put your python code here
lst = list(map(int, input().split()))
for i in range(len(lst)):
    for j in range(len(lst) - i - 1):
        if lst[j] > lst[j+1]:
            lst[j], lst[j+1] = lst[j+1], lst[j]
print(*lst)
