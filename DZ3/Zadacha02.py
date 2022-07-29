# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
'''
def dlb(lst: list) -> list:
    count_dbl = (len(lst) + 1) // 2
    res_list = [lst[i] * lst[-i - 1] for i in range(count_dbl)]
    return res_list


list_1 = [[2, 3, 4, 5], [2, 3, 4, 5, 6]]
print(list(map(dlb, list_1)))
'''
list_1 = [[2, 3, 4, 5], [2, 3, 4, 5, 6]]
'''
list_2 = []
x = len(List_1)//2 + 1
i = 0
while i < x:
    List_2.append(List_1[i]*List_1[-1-i])
    i += 1
print(List_2)
'''

def mult(lst: list):
    x = (len(lst) + 1) //2
    res = [lst[i]*lst[-1-i] for i in range(x)]
    return res
print(list(map(mult, list_1)))