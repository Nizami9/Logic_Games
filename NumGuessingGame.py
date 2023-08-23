import random
from art import logo2
from replit import clear
attempts = 0


def play_more():
    new_game = input("Do you wanna play one more time? Type yes or no: ")
    if new_game == 'yes':
        game()
    else:
        return print("Have a nice day!")


def check():
    global attempts
    level = input("Choose a difficulty: easy or hard? ")
    if level == 'easy':
        attempts += 10
    elif level == 'hard':
        attempts += 3
    else:
        print('Wrong level. Please choose correct level')
        check()


def game():
    print(logo2)
    global attempts
    print('Welcome to the Number Guessing Game!')
    print("I/'am thinking of a number between 1 and 100.")

    right_number = int(random.choice(range(10)))

    check()

    while attempts != 0:
        guess = int(input("Make a guess: "))
        if guess == right_number:
            print("Yo win!")
            return play_more()
        else:
            attempts -= 1
            differ = guess - right_number
            if differ > 5:
                print('Too high.')
            else:
                print('Too close.')
                print(f"Guess again.")
                print(f"You have {attempts} attempts remaining to guess the number")

    print(f"Right number was: {right_number}")
    clear()
    play_more()


game()
