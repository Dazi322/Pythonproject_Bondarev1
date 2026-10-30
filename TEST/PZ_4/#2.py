#  Дано целое число N (>0). С помощью операций деления нацело и взятия остатка от
# деления определить, имеется ли в записи числа N цифра «2». Если имеется, то
# вывести TRUE, если нет — вывести FALSE.



while True:
    
    try:
        n = int(input("Введи число:"))
        break
    except ValueError:
        print("Неправильно ввели!")


while n > 0:
    if n % 10 == 2: 
        break
    n //= 10  

if n > 0: 
    print("TRUE")
else:
    print("FALSE")