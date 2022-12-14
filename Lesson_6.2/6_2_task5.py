'''
Подвиг 7. Имеется словарь с наименованиями предметов и их весом (в граммах):

things = {'карандаш': 20, 'зеркальце': 100, 'зонт': 500, 'рубашка': 300, 
          'брюки': 1000, 'бумага': 200, 'молоток': 600, 'пила': 400, 'удочка': 1200,
          'расческа': 40, 'котелок': 820, 'палатка': 5240, 'брезент': 2130, 'спички': 10}
Сергей собирается в поход и готов взвалить на свои хрупкие плечи максимальный вес в N кг (вводится с клавиатуры). Он решил класть в рюкзак предметы в порядке убывания их веса (сначала самые тяжелые, затем, все более легкие) так, чтобы их суммарный вес не превысил значения N кг. Все предметы даны в единственном экземпляре. Выведите список предметов (в строчку через пробел), которые берет с собой Сергей в порядке убывания их веса.

P. S. 1 кг = 1000 грамм

Sample Input:

10
Sample Output:

палатка брезент удочка брюки пила карандаш спички
'''

# put your python code here
'''things = {'карандаш': 20, 'зеркальце': 100, 'зонт': 500, 'рубашка': 300, 
          'брюки': 1000, 'бумага': 200, 'молоток': 600, 'пила': 400, 'удочка': 1200,
          'расческа': 40, 'котелок': 820, 'палатка': 5240, 'брезент': 2130, 'спички': 10}
thing_rev = {value: key for key, value in things.items()}
N = int(input()) * 1000
sum = 0
lst = [things[i] for i in things]
lst.sort(reverse = True)
for i in lst:
    sum += i
    if sum < N:
        for j in things:
            if i == things[j]:
                print(j, end = " ")
    else:
        break'''


things = {'карандаш': 20, 'зеркальце': 100, 'зонт': 500, 'рубашка': 300, 
          'брюки': 1000, 'бумага': 200, 'молоток': 600, 'пила': 400, 'удочка': 1200,
          'расческа': 40, 'котелок': 820, 'палатка': 5240, 'брезент': 2130, 'спички': 10}

max_weight = int(input()) * 1000
equipment = list()


# создаём список и заносим туда все веса:
weight = list()
for value in things.values():
    weight.append(value)

    
# упорядочиваем их по убыванию:
weight.sort()
weight.reverse()

# определяем вес, который можем запихнуть:
take = 0
take_list = []

for item in weight:
    if take + item <= max_weight:
        take += item
    else:
        last_element = weight.index(item)
        break
           
if max_weight >= sum(weight):
    take_list = weight[:]
else:  # доберём ещё вещей:
    take_list = weight[:last_element]
    
# остались на выбор вещи:
    other = weight[last_element:]
# смотрим сколько осталось места:
    more = max_weight - sum(take_list)

# добавляем вещей по максимому:
    for thing in other:
        if thing <= more:
            take_list.append(thing)
            more -= thing

# добавляем в рюкзак вещи из списка:
for weight in take_list:
    for key, value in things.items():
        if weight == value:
            equipment.append(key)
            
print(*equipment)
