# !/usr/bin/env python3
# -*- encoding: utf-8 -*-

if __name__ == "__main__":
    number = int(input("Введите число:"))

l_card = ['Шесть','Семь','Восемь','Девять','Десять','Валет','Дама','Король','Туз']
number = int(input("Введите число:")) - 6
print(l_card[number])