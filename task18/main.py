"""
Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

*Пример:*

5
    1 5 3 10 7
    6
    -> 5
"""
import random

len_list = int(input('Enter length of list: '))
_list = []
for i in range(len_list):
    _list.append(random.randint(0, 10))
print(_list, end =' ')
print()
# _list = [2, 1, 9, 3, 4, 5, 8]
max_el = max(_list)
num = int(input('Enter the number: '))
for i in _list:
    if num < i:
        if i < max_el:
            max_el = i
print(max_el)

