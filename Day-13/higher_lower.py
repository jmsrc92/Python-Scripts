import random
import art
from game_data import data

score = 0

while score >= 0:
    print(art.logo)

    def random_number():
        """generates a random_number number from 0 to between list range"""
        global data
        generated_number = random.randint(0, len(data)-1)
        return generated_number


    def account_generator(rand_int):
        """returns a random account from given data list"""
        global data
        rand_account = data[rand_int]
        return rand_account


    first_account = account_generator(random_number())
    second_account = account_generator(random_number())

    if second_account == first_account:
        second_account = account_generator(random_number())

    def account_info(account):
        """prints details of account and returns followers"""
        account_name = account['name']
        account_description = account['description']
        account_country = account['country']
        account_followers = account['follower_count']
        string = (f"{account_name}, a {account_description},\
 from {account_country}")
        return account_followers, string

    account_1_followers, account_1_details = account_info(first_account)

    print(f"Compare A: {account_1_details}")

    print(art.vs)

    account_2_followers, account_2_details = account_info(second_account)

    print(f"Against B: {account_2_details}")
    print("")

    def compare_followers(total_a,total_b):# 10 , 20
        """returns A or B for final decision"""
        greater_total = ""
        if total_a > total_b:
            greater_total = "A"
        else:
            greater_total = "B"
        return greater_total

    result = compare_followers(total_a=account_1_followers,
    total_b=account_2_followers)

    usr_choice = input("Which is higher A or B?\
 Type answer as 'A' or 'B': ").upper()

    if usr_choice == result:
        score += 1
        print(f"\nYou guessed correct! Your score is {score}")

    else:
        print(f"\nYou lose your score was {score}")
        score = -1
