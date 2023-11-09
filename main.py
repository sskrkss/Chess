from new_game import new_game


def main():
    game = new_game.NewGame()
    while game.game_status == 'in progress':
        game.new_game()
    print('Игра окончена')

if __name__ == "__main__":
    main()
