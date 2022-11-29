#!/usr/bin/env python3
# импортирую функцию из модуля engine (общий для всех):
from brain_games.engine import start_game
# импортирую модуль из директории brain_games/games
from brain_games.games import even_game


def main():
    start_game(even_game)


if __name__ == '__main__':
    main()
