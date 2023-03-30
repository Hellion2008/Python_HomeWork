"""
Задача 32: Определить индексы элементов массива (списка), 
значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)
Ввод:  [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
Вывод: [1, 9, 13, 14, 19]
"""
import random
def list_index(lst, min_num, max_num):
    arr = []
    for i in range(len(lst)):
        if min_num <= lst[i] < max_num:
            arr.append(i)
    return arr

def random_list(n):
    arr = [random.randint(1,20) for i in range(n)]
    return arr

# a = [1, 5, 8, 12, 13, 7, 10, 11, 15]
a = random_list(10)
print(a)
min_num = int(input())
max_num = int(input())
print(list_index(a, min_num, max_num))

