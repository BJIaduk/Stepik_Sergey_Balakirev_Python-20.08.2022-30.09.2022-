'''
Подвиг 4. Имеется закодированная строка с помощью азбуки Морзе. 
Коды разделены между собой пробелом. Необходимо ее раскодировать, 
используя азбуку Морзе из предыдущего занятия. Полученное сообщение (строку) вывести на экран.

Sample Input:

.-- ... . -...- .-- . .-. -. ---
Sample Output:

все верно
'''

# put your python code here
# put your python code here
morze = {'а': '.-', 'б': '-...', 'в': '.--', 'г': '--.', 'д': '-..', 'е': '.', 'ж': '...-', 'з': '--..', 'и': '..', 'й': '.---', 'к': '-.-', 'л': '.-..', 'м': '--', 'н': '-.', 'о': '---', 'п': '.--.', 'р': '.-.', 'с': '...', 'т': '-', 'у': '..-', 'ф': '..-.', 'х': '....', 'ц': '-.-.', 'ч': '---.', 'ш': '----', 'щ': '--.-', 'ъ': '--.--', 'ы': '-.--', 'ь': '-..-', 'э': '..-..', 'ю': '..--', 'я': '.-.-', ' ': '-...-'}
morze_rev = {value: key for key, value in morze.items()}
lst = list(input().split())
lst = [ morze_rev.get(lst[i]) for i in range(len(lst))]
print(''.join(lst))