# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
#       - 6782 -> 23
#       - 0,56 -> 11

def get_count(number):
    s = str(number)
    if '.' in s:
        print (abs(s.find('.') - len(s)) - 1)
        return abs(s.find('.') - len(s)) - 1
    else:
        return 0
a = input("Введите число --> ")
x = int(get_count(a))
y = float(a)
if x != 0:
    for i in range(x):
        y *= 10
y = int(y)
b = 0
for i in range(len(a) - 1):
    b += y % 10
    y = y//10
print(b)