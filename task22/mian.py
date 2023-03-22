"""
Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n - кол-во элементов первого множества. 
m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.
"""

set_1 = int(input('enter the number N of elements of the first set: '))
set_2 = int(input('enter the number M of elements of the second set: '))
m = set()
n = set()
for i in range(set_1):
    m.add(int(input(f"element {i}: ")))
for i in range(set_2):
    n.add(int(input(f"element {i}: ")))
print(f'm: {m}      n: {n}')
res = m.intersection(n)
print(f'output elements -> {sorted(res)}')

# решение split(), не обращая внимания на n и m

# w1 = input("first list of numbers: ").split()
# w2 = input("second list of numbers: ").split()
# res = set(w1).intersection(set(w2))
# print(sorted(res))

# 2 вариант
# проверка на число и проверка на длину списка

# n = 5
# s = set()
# isLen = True
# while isLen:
#     w1 = input("first list of numbers: ").split()
#     for i in w1:
#         if i.isdigit():
#             s.add(int(i))
#     if len(s) != n:
#         print("ДЛИНА МАЛЕНЬКАЯ")
#     else:
#         isLen = False
    
# print(s)



