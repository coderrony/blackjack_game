
import random


def calculate_score(cards_list):
    if sum(cards_list) == 21 and len(cards_list) == 2:
        return 0
    if 11 in cards_list and sum(cards_list) > 21:
        cards_list.remove(11)
        cards_list.append(1)
    return sum(cards_list)


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "You Lose. opposite has blackjack"
    elif user_score == 0:
        return "you win with blackjack"
    elif user_score > 21:
        return "you went over you Lose"
    elif computer_score > 21:
        return "you win, the opposite went over"
    elif computer_score > user_score:
        return "you lose for low score"
    else:
        return "you win for high score"


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def game_start():
    user_cards = []
    computer_cards = []
    game_end = False

    for i in range(2):
        user_cards.append(random.choice(cards))
        computer_cards.append(random.choice(cards))

    while not game_end:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_end = True
        else:
            operation = input(
                "Type 'y' to get another card, type 'n' to pass:")
            if operation == 'y':
                user_cards.append(random.choice(cards))
            else:
                game_end = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(random.choice(cards))
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(
        f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


while (input("Do you want to play a game of Blackjack? Type 'y' or 'n':") == 'y'):
    game_start()
