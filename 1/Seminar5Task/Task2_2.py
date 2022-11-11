#Человек против человека

from random import choice, randint


message = ['твоя очередь,', 'бери конфеты,', 'бери больше,', 'ещё бери,',
           'бери быстрее,', 'ждём, играть и так долго,']


def player_vs_player():
    candies_total = 2021
    max_take = 28
    count = 0
    player_1 = input('\nКак тебя зовут? ')
    player_2 = input('\nА твоего соперника? ')

    print(f'\n{player_1} и {player_2}, начинаем играть\n')
    print('\nРазыгрываю, кто ходит первым.\n')

    x = randint(1, 2)
    if x == 1:
        lucky = player_1
        loser = player_2
    else:
        lucky = player_2
        loser = player_1
    print(f'Поздравляю, {lucky}, ты ходишь первым !')

    while candies_total > 0:
        if count == 0:
            step = int(input(f'\n{choice(message)} {lucky} = '))
            if step > candies_total or step > max_take:
                step = int(input(f'\nМожно взять только {max_take} конфет, {lucky}, вводи еще раз: '))
            candies_total = candies_total - step
        if candies_total > 0:
            print(f'\nна кону еще {candies_total}')
            count = 1
        else:
            print('Все конфеты разобрали')

        if count == 1:
            step = int(input(f'\n{choice(message)} {loser} '))
            if step > candies_total or step > max_take:
                step = int(input(f'\nМожно взять только {max_take} конфет, {loser}, попробуй еще раз: '))
            candies_total = candies_total - step
        if candies_total > 0:
            print(f'\nна кону еще {candies_total}')
            count = 0
        else:
            print('Все конфеты разобрали')

    if count == 1:
        print(f'{loser} победил')
    if count == 0:
        print(f'{lucky} победил')


player_vs_player()