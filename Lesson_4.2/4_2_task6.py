'''
Подвиг 6. Дата некоторого дня характеризуется двумя натуральными числами: m (порядковый номер месяца) и n (число). По введенным m и n (в одну строку через пробел) определить:

а) дату предыдущего дня (принять, что m и n не характеризуют 1 января);
б) дату следующего дня (принять, что m и n не характеризуют 31 декабря).

В задаче принять, что год не является високосным. Вывести предыдущую дату и следующую дату (в формате: mm.dd, где m - число месяца; d - номер дня) в одну строчку через пробел.

P.S. Число дней в месяцах не високосного года, начиная с января: 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31

Sample Input:

8 31

Sample Output:

08.30 09.01
'''

# put your python code here
mounth, day = map(int,input().split())
lst = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if (mounth == 1 or mounth == 3 or mounth == 5 or mounth == 7 or mounth == 8) and day == 31:
        print(f"0{mounth}.{day-1} 0{mounth+1}.01")
elif (mounth == 10 or mounth == 12) and day == 31:
    print(f"{mounth}.{day-1} {mounth+1}.01")
elif (mounth == 4 or mounth == 6) and day == 30:
        print(f"0{mounth}.{day-1} 0{mounth+1}.01")
elif mounth == 9 and day == 30:
    print(f"0{mounth}.{day-1} {mounth+1}.01")
elif (mounth == 11) and day == 30:
    print(f"{mounth}.{day-1} {mounth+1}.01")
elif mounth == 2 and day == 28:
        print(f"0{mounth}.{day-1} 0{mounth+1}.01")
elif day == 1:
    mounth -= 1
    if mounth == 1 or mounth == 3 or mounth == 5 or mounth == 7 or mounth == 8:
        print(f"0{mounth}.{31} 0{mounth+1}.0{day+1}")
    elif mounth == 10:
        print(f"0{mounth}.{31} {mounth+1}.0{day+1}")
    elif mounth == 12:
        print(f"{mounth}.{31} {mounth+1}.0{day+1}")
    elif mounth == 4 or mounth == 6:
        print(f"0{mounth}.{30} 0{mounth+1}.0{day+1}")
    elif mounth == 9:
        print(f"0{mounth}.{30} {mounth+1}.0{day+1}")
    elif mounth == 11:
        print(f"{mounth}.{30} {mounth+1}.0{day+1}")
    elif mounth == 2:
        print(f"0{mounth}.{28} 0{mounth+1}.0{day+1}")
elif 2 <= day <= 8:
    print(f"0{mounth}.0{day-1} 0{mounth}.0{day+1}")
elif day == 9:
    print(f"0{mounth}.0{day-1} 0{mounth}.{day+1}")
elif 1 <= mounth <= 9:
    print(f"0{mounth}.{day-1} 0{mounth}.{day+1}")
else:
    print(f"{mounth}.{day-1} {mounth}.{day+1}")


