"""Задание 1
Напишите программу, которая считывает одну строку. Если
это строка «Python», программа выводит «ДА», в противном случае программа
выводит «НЕТ».
"""

a=input()

if a == "python":
    print("ДА")
else:
    print("НЕТ")

"""
Задание 2
Напишите программу, которая определяет, состоит ли
двузначное число, введённое с клавиатуры, из одинаковых цифр. Если
состоит, то программа выводит «ДА», в противном случае программа выводит
«НЕТ».
"""
    
from math import floor


print("Enter the first Number")

a = input()

print("The first number is ",a)

print("Enter the second number")
b = input()

print("The second number is ",b)

if a==b:
    print("ДА")
else:
    print("НЕТ")

"""
Задание 3
Напишите программу, которая считывает три числа и
подсчитывает количество чётных чисел.
"""

even_count = 0
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the three number: "))

if num1 % 2 == 0:
    even_count = even_count + 1
if num2 % 2 == 0:
    even_count = even_count + 1
if num3 % 2 == 0:
    even_count = even_count + 1
    

print(even_count)
      
 
"""
Задание 9
Следующая формула может быть использована для
определения дня недели, соответствующего 1 января заданного года:
day_of_the_week = (year + floor((year – 1)/4) – floor((year – 1)/100) +
floor ((year – 1)/400))%7
В результате мы получим целое число, которое представляет день
недели от воскресенья (0) до субботу (6).
Используйте эту формулу для написания программы, которая
запрашивает у пользователя год и выводит на экран день недели, на который
в заданном году приходится 1 января. При этом на экране вы должны вывести
не числовой эквивалент дня недели, а его полное название.
"""


print("Enter the wanted year")
year = int(input("what year?: ")) 

day_of_the_week = day_of_the_week = (year+floor((year - 1)/4)-floor((year - 1)/100)+floor((year-1)/400))%7


if day_of_the_week == 1:
    print("1 января в понедельник")
elif day_of_the_week == 2:
     print("1 января во вторник")
elif day_of_the_week == 3:
    print("1 января в среда")
elif day_of_the_week==4:
    print("1 января в четверг")
elif day_of_the_week==5:
    print("1 января в пятница")
elif day_of_the_week==6:
    print("1 января в суббота")
elif day_of_the_week==0:
    print("1 января в воскресенье")
