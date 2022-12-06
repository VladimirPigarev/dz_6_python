# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# Использование функции filter
# РЕШЕНИЕ:
n = [int(input("Введите целое число n = "))]
print(n)
def poisk(mas1):
    rez = []
    i = 2
    while i <= mas1:
        if mas1 % i == 0:
            rez.append(i)
            mas1 //= i
        else:
            i += 1
    print(rez)
new_mas = filter(poisk, n)
print(list(new_mas))