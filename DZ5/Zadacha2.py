# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, 
# чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота

# b) Подумайте как наделить бота ""интеллектом""

number_of_candies = 2021

player = 1
x = 0
y = 0

while number_of_candies != 0:
    if player == 1:
        x = int(input('Берет первый игрок конфеты '))
        number_of_candies = number_of_candies - x
        if number_of_candies == 0:
            print('Выиграл Первый игрок')
        print(f'Конфет осталось_' + str(number_of_candies))
        player = 2
    else:
        y = int(input('Берет второй игрокконфеты '))
        number_of_candies = number_of_candies - y
        if number_of_candies == 0:
            print('Выиграл Второй игрок')
        print(f'Конфет осталось_' + str(number_of_candies))
        player = 1