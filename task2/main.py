"""
Найдите сумму цифр трехзначного числа.

*Пример:*

123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0) |
"""
num = int(input("Enter your number: "))
result = num // 100 + (num % 100) // 10 + num % 10
print(f"{num} -> {result}")
