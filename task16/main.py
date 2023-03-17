"""
Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

*Пример:*

5
    1 2 3 4 5
    3
    -> 1

"""
import random
len_list = int(input('Enter length of list: '))
_list = []
for i in range(len_list):
    _list.append(random.randint(0, 10))
print(_list, end =' ')
print()

num = int(input('Enter the number: '))
count = len([i for i in _list if i == num])
print(count)

