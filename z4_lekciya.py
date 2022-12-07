# В файле хранятся числа, нужно выбрать четные и составить список пар (число, квадрат числа).
# Пример: 1, 2, 3, 5, 8, 15, 23, 38
# [(2, 4), (8, 64), (38, 1444)]

mas = [1, 2, 3, 5, 8, 15, 23, 38]
mas_result = []
for i in range(len(mas)):
    if mas[i]%2 == 0:
        mas_result.append(mas[i])
print(mas_result)
def f(x):
    return x**2
mas_result = [(i, f(i)) for i in mas_result]
print(mas_result)