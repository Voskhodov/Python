# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

My_list = [2, 3, 5, 9, 3]
x = 0
for item in range(len(My_list)):
    if item%2 != 0:
        x += My_list[item]
print(x)