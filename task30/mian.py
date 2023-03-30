"""
Задача 30: Заполните массив элементами арифметической прогрессии. 
Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: 
an = a1 + (n-1) * d.
Каждое число вводится с новой строки.
Ввод: 7 2 5
Вывод: 7 9 11 13 15
"""
def list_arr(a, d, n):
    res = []
    for i in range(n):
        res.append(a + i * d)
    return res

a = int(input('Enter start number a: '))
d = int(input('Enter difference d: '))
n = int(input('Enter count of numbers n: '))
print(list_arr(a, d, n))

