# Составить функцию, которая выполнит суммирования числового ряда.

def sum_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

numbers = [1, 5, 10, 20]
print(sum_list(numbers))  
