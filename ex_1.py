# !/usr/bin/env python3
# -*- encoding: utf-8 -*-

if __name__ == "__main__":
    month = int(input("Введите месяц:"))
    year = int(input("Введите год:"))

    if month > 12 or month < 1:
        print("Не может быть такого значения")
    else:
        if month == 2:
            if (year % 400 == 0 and year % 100 == 0) or (year % 4 == 0 and year % 100 != 0):
                print(29)
            else:
                print(28)
        elif month in [1, 3, 5, 7, 8, 10, 12]:
            print(31)
        else:
            print(30)
    print('Конец программы')