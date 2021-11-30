# !/usr/bin/env python3
# -*- encoding: utf-8 -*-

if __name__ == "__main__":
    m = int(input())
    n = int(input())
    g = int(input())
    n_d = 0
    p_d = 0
    date = 0
    finish = 0
    g1 = g
    if ( g % 100 != 0 and g % 4 == 0) or (g % 100 == 0 and g % 400 == 0):
        month_febr = 29
    else:
        month_febr = 28
    if m == 2:
        finish = month_febr
    elif m in [1, 3, 5, 7, 8, 10, 12]:
        finish = 31
    else:
        finish = 30
    if n > finish or n < 1:
        print("Нет такого значения")
    else:
        if n == 1:
            n_d = 2
            m1 = m - 1
            if m1 in [1, 3, 5, 7, 8, 10, 12]:
                p_d = 31
            elif m1 == 2:
                p_d = month_febr
            else:
                p_d = 30
            if m1 == 0:
                m1 = 12
                g1 -= 1
                p_d += 1
            print(f"Previous day is {p_d}.{m1}.{g1}")
            print(f"Next day is {n_d}.{m}.{g}")
        elif n == finish:
            m1 = m + 1
            p_d = n - 1
            n_d = 1
            if m1 == 13:
                m1 = 1
                g1 += 1
            print(f"Previous day is {p_d}.{m}.{g}")
            print(f"Next day is {n_d}.{m1}.{g1}")
        else:
            print(f"Previous day is {n - 1}.{m}.{g}")
            print(f"Next day is {n + 1}.{m}.{g}")

