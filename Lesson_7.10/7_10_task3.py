'''
Подвиг 3. Используя замыкания функций, объявите внутреннюю функцию, которая заключает в тег h1 строку s (s - строка, параметр внутренней функции). Далее, на вход программы поступает строка и ее нужно поместить в тег h1 с помощью реализованного замыкания. Результат выведите на экран.

P. S. Пример добавления тега h1 к строке "Python": <h1>Python</h1>

Sample Input:

Balakirev
Sample Output:

<h1>Balakirev</h1>
'''

# put your python code here
def func1(teg = "h1"):
    def func2(s):
        return f"<{teg}>{s}</{teg}>"
    return func2
st = input()
cnt = func1()
print(cnt(st))
