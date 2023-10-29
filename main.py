import new_game

if __name__ == '__main__':
    new_game = new_game.NewGame()
    print(new_game)
    print()
    new_game.move(1, 0, 4, 0)
    print(new_game)