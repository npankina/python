# -*- coding: utf-8 -*-
"""
    Год високосный, если он делится на четыре без остатка,
    но если он делится на 100 без остатка, это не високосный год.
    Однако, если он делится без остатка на 400, это високосный год.
"""

while True:
    try:
        year = int(input("Enter a year: "))

        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    print(f"{year} is leap year.")
                else:
                    print(f"{year} ISN'T leap year.")
            else:
                print(f"{year} is leap year.")
        else:
            print(f"{year} ISN'T leap year.")
    except KeyboardInterrupt:
        break