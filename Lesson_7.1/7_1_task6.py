'''
Подвиг 8. Напишите функцию, которая проверяет корректность переданного ей email-адреса в виде строки. Будем полагать, что адрес верен, если он обязательно содержит символы '@' и '.', а все остальные символы могут принимать значения: 'a-z', 'A-Z', '0-9' и '_'. Если email верен, то функция выводит ДА, иначе - НЕТ.

После объявления функции прочитайте (с помощью функции input) строку с email-адресом и вызовите функцию с этим аргументом.

Sample Input:

sc_lib@list.ru
Sample Output:

ДА
'''

# put your python code here
def correct_email(email):
    flag = True
    for i in email:
        if ('a' < i < 'z' or 'A' < i < 'Z' or '0' < i < '9' or i == '_' or i == '@' or i == '.'):
            flag = True
        else:
            flag = False
            break
            
    if flag and email.count('@') != 0 and email.count('.') != 0:
        print("ДА")
    else:
        print("НЕТ")
    
email = input()
correct_email(email)
