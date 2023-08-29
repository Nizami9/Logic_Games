from art import logo3, vs
import random
from game_data import data
from replit import clear


def get_random_account():
    return random.choice(data)


def data_form(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"


def check_answer(answer, a_follower_count, b_follower_count):
    if a_follower_count > b_follower_count:
        return answer == "a"
    else:
        return answer == "b"


def game():
    print(logo3)
    score = 0
    game_should_continue = True
    account1 = get_random_account()
    account2 = get_random_account()

    while game_should_continue:
        account1 = account2
        account2 = get_random_account()

        while account1 == account2:
            account2 = get_random_account()

        print(f"Compare A: {data_form(account1)}")
        print(vs)
        print(f"Against B: {data_form(account2)}")

        answer = input("Who has more followers? Type 'A' or 'B': ").lower()
        a_follower_count = account1["follower_count"]
        b_follower_count = account2["follower_count"]
        is_correct = check_answer(answer, a_follower_count, b_follower_count)

        clear()
        print(logo3)
        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            game_should_continue = False
            print(f"Sorry, that's wrong. Final score: {score}")


game()