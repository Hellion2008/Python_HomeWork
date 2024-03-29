"""
В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, 
причем кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два 
соседних. Всего на грядке растет N кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное
 число ягод – на i-ом кусте выросло ai ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
Эта система состоит из управляющего модуля и нескольких собирающих модулей. Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод, которое может собрать 
за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном 
файле грядки.
"""
import random
num = int(input('Enter count of bushs: '))
lst_berry = list()
for i in range(num):
    lst_berry.append(random.randint(1, 10))
print(lst_berry)

lst_max = list()
lst_max.insert(0, lst_berry[-1] + lst_berry[0] + lst_berry[1])
lst_max.insert(len(lst_berry) - 1, lst_berry[len(lst_berry) - 2] + lst_berry[len(lst_berry) - 1] + lst_berry[0])
for i in range(1, len(lst_berry) - 1):
    lst_max.insert(i, lst_berry[i - 1] + lst_berry[i] + lst_berry[i + 1])

print(lst_max)
print(max(lst_max))

