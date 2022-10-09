'''
Подвиг 6. Вводятся данные в формате ключ=значение в одну строчку через пробел. Необходимо на их основе создать словарь d, затем удалить из этого словаря ключи 'False' и '3', если они существуют. Ключами и значениями словаря являются строки. Вывести полученный словарь на экран командой:

print(*sorted(d.items()))

Sample Input:

лена=имя дон=река москва=город False=ложь 3=удовлетворительно True=истина

Sample Output:

('True', 'истина') ('дон', 'река') ('лена', 'имя') ('москва', 'город')
'''

# put your python code here
lst_in = list(input().replace("=", " ").split())
lst_in = [ [ lst_in[i],  lst_in[i+1]] for i in range(0, len(lst_in) - 1, 2) ]
#print(lst_in)
d = dict(lst_in)
if ("False" in d):
    del d["False"]
if ('3' in d):
    del d['3']
print(*sorted(d.items()))

#d = dict([i.split('=') for i in input().split()])
