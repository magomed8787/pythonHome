# Задача 1.................................................................................
# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и
# проверяет, является ли этот день выходным.

# day = int(input())
# if day > 5 and day <= 7:
#     print("да, день выходной")
# if day <= 0 or day > 7:
#     print("введит цифру обозначающую день недели")
# else:
#     print("нет, день рабочий")

# Задача 2................................................................................
# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z (расшифровка этого выражения
# not (x[0] or x[1] or x[2] = not x[0] and not x[1] and not x[2]) для всех значений предикат.
# for x in range(0, 2):
#         for y in range(0, 2):
#             for z in range(0, 2):
#                 print(not (x or y or z) == (not x and not y and not z))
#                 print(x, y, z)

# Задача 3................................................................................
# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти
# плоскости, в которой находится эта точка.

# x = int(input())
# y = int(input())
# while x !=0 and y != 0:
#     if x > 0 and y > 0:
#         print("точка находится в 1-й четверти")
#         break
#     elif x < 0 and y > 0:
#         print("точка находится во 2-й четверти")
#         break
#     elif x < 0 and y < 0:
#         print("точка находится в 3-й четверти")
#         break
#     elif x > 0 and y < 0:
#         print("точка находится в 4-й четверти")
# else:
#     print("Введите координаты соответствующие условию задачи")

# Задача 4.............................................................................
# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек
# в этой четверти (x и y).

# x = int(input("Введите номер четверти: "))
# if x == 1:
#     print("Диапазон возможных координат: x > 0, y > 0")
# if x == 2:
#     print("Диапазон возможных координат: x < 0, y > 0")
# if x == 3:
#     print("Диапазон возможных координат: x < 0, y < 0")
# if x == 4:
#     print("Диапазон возможных координат: x > 0, y < 0")

# Задача 5............................................................................
# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

# list1 = []
# list2 = []
# for i in range(0, 2):
#     list1.append(int(input()))
# for i in range(0, 2):
#     list2.append(int(input()))
# L = (((list2[0] - list1[0])**2) + ((list2[1] - list1[1])**2)) ** 0.5
# print("Расстояние между двумя точками равно: ", int(L * 100) / 100)

# a = [int(i) for i in input().split()]
# b = len(a)
# n = []
# for i in range(b):
#     if a[i] != a[-1]:
#         n.append(a[i-1] + a[i+1])
#     if a[i] == a[-1]:
#         n.append(a[-2] + a[0])
# print(n)



# /////////////////////////////////////Seminar 2////////////////////////////////////////

# Задача 1...........................
# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

# a = input()
# count = 0
# for i in a:
#     count += int(i)
# print(count)

# Задача 2...............................
#Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# n = int(input("Введите число: "))
# array = []
# count = 1
# for i in range(1, n+1):
#     count = i * count
#     array.append(count)
# print(*array)


# Задача 3.
# Задайте список из n чисел последовательности (1+(1/n))**n и выведите на экран их сумму
# Пример: Для n = 4 {1:2, 2: 2.25, 3: 2.37, 4: 2.44}. Сумма 9.06

# n = int(input())
# array = []
# count = 0
# for i in range(1, n+1):
#     array.append((((1+(1/i))**i)))
# for i in array:
#     count+=i
# print(int(count*100)/100)

# Задача 4.
# Реализуйте алгоритм перемешивания списка.
# a = [int(i) for i in input().split()]
# for i in range(len(a)):
#     import random
#     index = random.randint(0, len(a)-1)
#     a[i], a[index] = a[index], a[i]
#     # temp = a[i]
#     # a[i] = a[index]
#     # a[index] = temp
# print(a)

# /////////////////////////////////////Seminar 3////////////////////////////////////////

# Задача 1.
#Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на
# нечётной позиции.

# array = [int(i) for i in input("Введите значения списка: ").split()]
# count = 0
# for i in range(len(array)):
#     if i%2 != 0:
#         count += array[i]
#     else:
#         continue
# print(f"Сумма элементов списка стоящих на нечетной позиции, равна {count}")

# Задача 2.
#Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй
# и предпоследний и т.д.

# array = [int(i) for i in input("Введите значения списка: ").split()]
# new_array = []
# while len(array) > 1:
#     new_array.append(array[0]*array[len(array)-1])
#     array.pop(0)
#     array.pop(len(array)-1)
#     if len(array) == 1:
#         new_array.append(array[0] ** 2)
#         break
# print(new_array)

# array = [int(i) for i in input("Введите значения списка: ").split()]
# result = 0
# while len(array) > 1:
#     result = array[0]*array[len(array)-1]
#     array.pop(0)
#     array.pop(len(array)-1)
#     print(result, end = " ")
#     if len(array) == 1:
#         result = array[0] ** 2
#         print(result)
#         break

# Задача 3.
#Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным
# значением дробной части элементов.
# array = [float(i) for i in input("Введите значения списка: ").split()]
# new_array = []
# for i in range(len(array)):
#     new_array.append(float(array[i])-int(array[i]))
# print(round(max(new_array) - min(new_array),2))

# Задача 4.
# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# number = int(input("Введите десятичное число: "))
# while number != 1:
#     if number%2 != 0:
#         print(1, end = "")
#         number = (number-1)/2
#     else:
#         print(0, end = "")
#         number = number/2

# number = int(input("Введите десятичное число: "))
# while number != 1:
#     print(number % 2, end = "")
#     number = number // 2

# Задача 5.
# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# def fibonacci(number):
#     array = []
#     for i in range(0, number+1):
#         array.append(i)
#     for i in range(len(array)):
#         if array[i] == 0 or array[i] == 1:
#             continue
#         else:
#             array[i] = array[i-1]+array[i-2]
#     return array
#
# f1 = fibonacci(8)
# f1.reverse()
# f2 = fibonacci(8)[1:]
# for i in range(len(f1)):
#     if i%2 == 0:
#         f1[i] = -abs(f1[i])
#     else:
#         continue
# print(f1+f2)

# def fibonacci(num):
#     # num = int(input("Введите любое натуральное число: "))
#     fib = []
#     a, b = 1, 1
#     for i in range(num):
#         fib.append(a)
#         a, b = b, a+b
#     a, b = 0,1
#     for j in range(num+1):
#         fib.insert(0, a)
#         a, b = b, a-b
#     print(f"Список чисел Фибоначчи для {num}: {fib}")
#
# fibonacci(8)

# /////////////////////////////////////Seminar 4////////////////////////////////////////
#
# Задача 1.
# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# number = int(input())
# array = []
# d = 2
# while d <= number:
#     if number%d == 0:
#         array.append(d)
#         number = number/d
#     else:
#         d+=1
# print(array)

# Задача 2.
# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной
# последовательности.

# array = [int(i) for i in input("Введите значения списка: ").split()]
# new_array = []
# for i in array:
#     if array.count(i) == 1:
#         new_array.append(i)
#     else:
#         continue
# print(new_array)

# Задача 4.
# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

with open('file1.txt', 'w', encoding='utf-8') as file:
    file.write('2*x^2 + 5*x^5')
with open('file2.txt', 'w', encoding='utf-8') as file:
    file.write('3*x**4 + 9*x**6')

with open('file1.txt','r') as file:
    file1 = file.readline()
    list_file1 = file1.split()


with open('file2.txt','r') as file:
    file2 = file.readline()
    list_file2 = file2.split()

print(f'{list_file1} + {list_file2}')
sum_poly = list_file1 + list_file2

with open('sum_file.txt', 'w', encoding='utf-8') as file:
    file.write(f'{list_file1} + {list_file2}')










