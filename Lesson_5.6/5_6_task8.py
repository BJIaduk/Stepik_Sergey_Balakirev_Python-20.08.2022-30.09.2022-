'''
Подвиг 8. В некоторой стране используются денежные купюры достоинством в 1, 2, 4, 8, 16, 32 и 64. 
Вводится натуральное число n. Как наименьшим количеством таких денежных купюр можно выплатить сумму 
n? Вывести на экран список купюр для формирования суммы n (в одну строчку через пробел, 
начиная с наибольшей и заканчивая наименьшей). Предполагается, что имеется достаточно 
большое количество купюр всех достоинств.

Sample Input:

221

Sample Output:

64 64 64 16 8 4 1
'''

# put your python code here
n = int(input())
lst = []
a = int(n/64)
a1 = int((n - a*64)/32)
b = int( (n - a*64 - a1*32) / 16 )
#print(b)
c = int((n - a*64 - a1*32 - b*16)/8)
d = int((n - a*64 - a1*32 - b*16 - c*8)/4)
d1 = int((n - a*64 - a1*32 - b*16 - c*8 - d*4)/2)
e = int((n - a*64 - a1*32 - b*16 - c*8 - d*4 - d1*2))
for x in range(a):
    lst.append(64)
for x in range(a1):
    lst.append(32) 
for x in range(b):
    lst.append(16) 
for x in range(c):
    lst.append(8) 
for x in range(d):
    lst.append(4)
for x in range(d1):
    lst.append(2) 
for x in range(e):
    lst.append(1) 

print(*lst)