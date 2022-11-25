#!/usr/bin/env python3
# импортирую функцию из модуля engine (общий для всех):
from brain_games.engine import check_result
# импортирую модуль из директории brain_games/games
from brain_games.games import Calc_try


def main():
    check_result(Calc_try)


if __name__ == '__main__':
    main()
