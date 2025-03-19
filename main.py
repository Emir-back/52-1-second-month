import configparser
from logic import play_game

def load_settings():
    config = configparser.ConfigParser()
    config.read('settings.ini')

    min_number = int(config['game_settings']['min_number'])
    max_number = int(config['game_settings']['max_number'])
    attempts = int(config['game_settings']['attempts'])
    initial_capital = int(config['game_settings']['initial_capital'])

    return min_number, max_number, attempts, initial_capital

if __name__ == '__main__':
    play_game()