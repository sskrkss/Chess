from game import Game


def main():
    print(f'Игра началась', end='\n\n')
    game = Game()
    while game.status in ('Ход белых', 'Ход черных'):
        game.cycle()
    print(f'Игра окончена. {game.status}')


if __name__ == "__main__":
    main()
