# Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5.3, 10.01] => 0.19

my_list = [1.1, 1.2, 3.1, 5.3, 10.01]
my_list1 = []
for i in range(len(my_list)):
    x = my_list[i]
    y = int(x)
    my_list1.append(x - y)
    round(my_list1[i], 2)
a = max(my_list1)
b = min(my_list1)
z=round(a-b, 3)
print(z)