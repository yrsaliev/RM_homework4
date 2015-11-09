## -*- coding: utf-8 -*-

# Переписать первое задание используя генераторы списков
# yt понятно где использовать ГС

from check import checking_input

while True:
    try:
        x=int(raw_input("Enter a number between 1 and 9: "))
        break
    except:
        print "It is not a number... Try again..."



checking_input.check_input(x)
