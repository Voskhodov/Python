# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
#   - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

num_fib = int(input('Введите число  '))
list_fibanachi = [0]
x = y = 1 
list_fibanachi.append(x)
list_fibanachi.append(y*-1)
if num_fib < 2:
    print(list_fibanachi)
else:
    for i in range(num_fib - 2):    # (-2) уже заданы два перых числа
    
        y, x = x, (x + y)# y приравнивается к x, x приравнивается к x + y
        list_fibanachi.append(x)
        if x > 0 and y > 0:
            x*= -1
            y*= -1
        else:
            x*= -1
            y*= -1

    list_fibanachi.reverse()
    
    x = y = 1 
    list_fibanachi.append(x)
    list_fibanachi.append(y)
    for i in range(num_fib - 2):    # (-2) уже заданы два перых числа
    
        y, x = x, (x + y)# y приравнивается к x, x приравнивается к x + y
        list_fibanachi.append(x)
    print(list_fibanachi)
