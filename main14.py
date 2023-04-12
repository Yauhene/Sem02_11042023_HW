# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

print()
N = int(input("Ведите целое число : "))
flag = True
n = 0
while flag:
    result = 2**(n)
    if result <= N:
        print(f' Два в степени {n} = {result};')
        n += 1
    else:
        flag = False
print()