import random
import configparser


config = configparser.ConfigParser()
config.read('settings.ini')


min_number = int(config['game_settings']['min_number'])
max_number = int(config['game_settings']['max_number'])
attempts = int(config['game_settings']['attempts'])
initial_capital = int(config['game_settings']['initial_capital'])


def play_game():
    capital = initial_capital
    print(f"Начальный капитал: {capital}")
    print(f"Вы должны угадать число от {min_number} до {max_number}.")

    for attempt in range(attempts):
        bet = int(input(f"Попытка {attempt + 1}. Ваш капитал: {capital}. Введите вашу ставку: "))
        if bet > capital:
            print("У вас недостаточно капитала для этой ставки.")
            continue

        number_to_guess = random.randint(min_number, max_number)
        guess = int(input(f"Угадайте число между {min_number} и {max_number}: "))

        if guess == number_to_guess:
            capital += bet
            print(f"Поздравляем! Вы угадали число! Ваш капитал: {capital}.")
        else:
            capital -= bet
            print(f"Не угадали! Загаданное число было: {number_to_guess}. Ваш капитал: {capital}.")

        if capital <= 0:
            print("У вас закончились деньги! Игра окончена.")
            break

    if capital > 0:
        print(f"Игра окончена. Ваш капитал: {capital}.")
