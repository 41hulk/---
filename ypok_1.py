"""
Задание 2
Напишите программу, которая определяет, состоит ли
двузначное число, введённое с клавиатуры, из одинаковых цифр. Если
состоит, то программа выводит «ДА», в противном случае программа выводит
«НЕТ».

"""
    
a=0
b=0

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
    
