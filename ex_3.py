# !/usr/bin/env python3
# -*- encoding: utf-8 -*-

if __name__ == "__main__":
    k = int(input("Введите число:"))
    day = 0
    if k % 7 == 0:
        print("Воскресенье")
    elif k % 7 != 0:
        day = k % 7
    elif k <= 7:
        day = k
    else:
        day = k / 7
    days = ["Понедельник","Вторник","Среда","Четверг","Пятница","Суббота"]
    print(days[int(day) - 1])