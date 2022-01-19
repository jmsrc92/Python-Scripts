import random

"""
dealer card shown
take a new card
store cards
if >21 lose
"""
card_list = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, ]  # Ace through king


def get_random_card(player_card_total=0):
    random_card = random.choice(card_list)
    if player_card_total >= 11:
        if random_card == 11:
            random_card = 1
    return random_card


def cards_total(list_of_cards):  # take list of cards loop and total them
    sum_of_cards = 0
    for card_val in list_of_cards:
        sum_of_cards += card_val
    return sum_of_cards


def check_ace(player):
    """Converts players card to 1 if over 11"""
    if player[-1] == 11:
        player[-1] = 1


players = {
    "player_1": [],
    "dealer": []

}

# Two random cards for player
players["player_1"].append(get_random_card())
players["player_1"].append(get_random_card())

# Random card for dealer
players["dealer"].append(get_random_card())

# Game start!!
print("Welcome to Black Jack")
print(f'Your cards are {players["player_1"]}')
print(f'The dealer has {players["dealer"]}')

# player card choice
while cards_total(players["player_1"]) <= 21:
    player_card_total = cards_total(players["player_1"])
    print(cards_total(players["player_1"]))
    choice = input("Do you wish to take another card? 'y' or 'n' : ")
    if choice == "y":
        players["player_1"].append(get_random_card(player_card_total))
        print(f'You now have {players["player_1"]}')
        if cards_total(players["player_1"]) > 21:
            print("You have gone bust dealer wins!")
            break
        if cards_total(players["player_1"]) == 21:
            print("You have 21!!")
            break
    else:
        print(f'You have stuck on {players["player_1"]} \
 = {cards_total(players["player_1"])}')
        break

player_card_sum = cards_total(players["player_1"])

dealer_bust = False

if player_card_sum > 21:
    dealer_bust = True

while not dealer_bust:
    dealer_sum = cards_total(players["dealer"])
    print(f'The dealers hand is {players["dealer"]}')
    if cards_total(players["dealer"]) < player_card_sum:
        players["dealer"].append(get_random_card(dealer_sum))
    elif cards_total(players["dealer"]) > 21:
        print("Dealer bust You Win!!")
        dealer_bust = True
    elif cards_total(players["dealer"]) == player_card_sum:
        print(f'Dealer has {players["dealer"]} game is a draw')
        dealer_bust = True
    else:
        # (cards_total(players["dealer"]) > player_card_sum and
        # cards_total(players["dealer"]) < 21):
        print("You Lose, Dealer Wins!")
        break

print("Game Over")
print("Want to play again")
