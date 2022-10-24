# 30. Вычислить число c заданной точностью d
# А так можно было сделать?
n = float(input('Введите число: '))
x = int(input('Введит до какого знакa после , округлить '))
#
print(round(n ,x))


# n = float(input('Введите число: '))
# x = int(input('Введит до какого знакa округлить '))
# if x == 1:
#     print(int(x))
# else:
#     x = str(x)
#     x = x.split('.')
#     x = len(x[1])
#     print(round(n, x))

# 31 Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N..

# n = int(input('Введите число от 1 до 1000: '))
# x = list(range(1, 1001))
#
# for i in range(1, len(x)):
#     if n % x[i] == 0 and i+1 != n:
#         # print(x[i])
#         print(i + 1)

# n = int(input())
# a = []
# for i in range(2, n + 1):
#     if n % i == 0:
#         for j in range(2, i // 2 + 1):
#             if i % j == 0:
#                 break
#         else:
#             a.append(i)
# print(a)

# # 32. Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.

# a = [12, 12, 12, 23, 23, 43, 34, 23, 43]
# b = []
# for i in a:
#     if i not in b:
#         b.append(i)
#
# print(b)

# a = [12, 12, 12, 23, 23, 43, 34, 23, 43]
# b = []
# for i in a:
#     if a.count(i) == 1:
#         b.append(i)
# print(b)
#

# 33. Задана натуральная степень k. Сформировать
# случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.

#
import random
some_dict = {0: '⁰', 1: '¹', 2: '²', 3: '³', 4: '⁴', 5: '⁵', 6: '⁶', 7: '⁷', 8: '⁸', 9: '⁹'}
k = int(input('Введите натуральную степень к: '))
coef = [random.randint(0, 100) for _ in range(k + 1)]
print (coef)
with open('coef.txt', 'w', encoding= 'utf-8') as m:
    for i in range(len(coef)):
        if k - i != 1 and k - i != 0:
            m.write(f'{coef[i]}x{some_dict[k - i]} + ')
        elif k - i == 1:
            m.write(f' {coef[i]}x + ')
        elif k - i == 0:
            m.write(f'{coef[i]} = 0')