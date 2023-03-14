"""
Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
Определите минимальное число монеток, которые нужно перевернуть, 
чтобы все монетки были повернуты вверх одной и той же стороной. 
Выведите минимальное количество монет, которые нужно перевернуть
"""
count_of_coins = int(input('Enter number of coins: '))
coins_list = []
for i in range(count_of_coins):
    coin = int(input(f'{i}: '))
    coins_list.append(coin)
print(coins_list)

count = 0
for i in coins_list:
    if i > 0:
        count += 1
print(count if count < len(coins_list)/2 else len(coins_list) - count)
