# 1.  Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
#  стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# n = [5, 7, 1, 3, 4, 6, 8]
# #print(n)
# summ = 0
# for i in range(1, len(n), 2):
#     #if i % 2 == 1:
#         summ += n[i]       
# print(f"{n} -> сумма элементов на нечётных позициях: {summ}")

# 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и 
# последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# from random import randint


# number = int(input('Введите размер списка: '))
# list = []
# list2 = []

# for i in range(number):
#     list.append(randint(0, 9))

# for i in range(len(list)):
#     while i < len(list)/2 and number > len(list)/2:
#         number = number - 1
#         a = list[i] * list[number]
#         list2.append(a)
#         i += 1

# print(list)
# print(list2)

# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным
#  и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# from random import uniform

# n = int(input('Введите размер списка '))
# list1 = []
# for i in range(n):
#     f = uniform(0, 9)
#     list1.append(round(f, 2))

# min = list1[0]
# max = 0
# for i in range(len(list1)):
    
#     if max < list1[i]:
#         max = list1[i]
#     if min > list1[i]:
#         min = list1[i]
# dif = (max - int(max)) - (min - int(min))

# print(list1)
# print(max, min)
# print(round(dif,2))


# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# a = ""
# n = int(input("Введите число для преобразовывания десятичного числа в двоичное:\n"))
# while n != 0:
#     a = str(n%2) + a
#     n //=2
# print(a)

# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.ДОП

# Пример:

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
#  [Негафибоначчи]

# n = int(input('Введите число: '))

# def get_fibonacci(n):
#     fibo_nums = []
#     a, b = 1, 1
#     for i in range(n-1):
#         fibo_nums.append(a)
#         a, b = b, a + b
#     a, b = 0, 1
#     for i in range (n):
#         fibo_nums.insert(0, a)
#         a, b = b, a - b
#     return fibo_nums

# fibo_nums = get_fibonacci(n)
# print(get_fibonacci(n))
# print(fibo_nums.index(0))

# 6. Суперсдвиг
# Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность 
# (сдвиг - циклический) на |K| элементов вправо, если K – положительное и влево, если отрицательное.

# Примеры
# №	INPUT.TXT	OUTPUT.TXT
# 	5
#   5 3 7 4 6
# 	3            7 4 6 5 3
# 	
#   5
#   5 3 7 4 6
#   -3           4 6 5 3 7

# input()
# a = input().split(' ')
# k = int(input())
# print(*a[-k:], end=' ')
# print(*a[0:-k])