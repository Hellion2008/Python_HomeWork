"""
Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

"""
num = int(input('Enter number: '))
index = 0
res = 1
while res <= num:  
    print(res, end=' ')
    index += 1
    res = 2 ** index
    

