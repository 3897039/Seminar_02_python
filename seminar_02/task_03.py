# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), 
# не превосходящие числа N.

N = int(input("Введите число N -> "))
degree = 2
k = 0
while degree ** k <= N:
    print(degree ** k)
    k += 1