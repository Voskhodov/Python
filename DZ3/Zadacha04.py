# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10
while True: # бесконечный цикл

    n = int(input("Введите число -->"))
    x = n
    bin_number = []
    if n == exit:
        break
    while n > 0:
        bin_number.append(n % 2)
        n = n // 2
    bin_number.reverse()
    print(bin_number)
    print("Для выхода наберите \"exit\" ")