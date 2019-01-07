from random import randint


def greetings():
    name = input('What is your name?\n>>> ')
    print(f'Hello, {name}')


def ask_player_for_number():
    return input('Give your number, from 1 to 10\n>>> ')


def user_wants_to_play(decision):
    if decision == 'no':
        return False
    elif decision == 'yes':
        print('Ok, lets go')
    else:
        print("I do not understand, so let's play again")
    return True


def game_result(lottery_win):
    while ask_player_for_number() != lottery_win:
        decision = input('Wrong, do you want to play again?\n>>> ')
        if not user_wants_to_play(decision):
            print(f'The secret number was: {lottery_win}')
            return False
    return True


if __name__ == "__main__":
    greetings()
    lottery_win = str(randint(1, 10))
    if game_result(lottery_win):
        print('💰💰💰💰 Congratulations! 💰💰💰💰')
    else:
        print('🔥🔥🔥🔥 You lost! 🔥🔥🔥🔥')
