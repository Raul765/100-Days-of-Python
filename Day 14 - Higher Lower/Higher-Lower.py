import os
from art import logo, vs
from data import data
import random

def clear ():
    os.system("cls")

def compare ():
    option_a=random.choice(data)
    option_b=random.choice(data)
    while option_a==option_b:
        option_b=random.choice(data)

    print(f"Compare A: {option_a['name']}, a {option_a['description']} from {option_a['country']}.")
    print(vs)
    print(f"Against B: {option_b['name']}, a {option_b['description']} from {option_b['country']}.")
    selection=input("Who has more followers? Type A or B: ").upper()

    if selection=="A" and option_a['follower_count']>option_b['follower_count']:
        correct=True
    elif selection=="B" and option_b['follower_count']>option_a['follower_count']:
        correct=True
    else:
        correct=False

    return correct

def game():
    correct=True
    score=0

    while correct==True:
        clear()
        print(logo)
        if score>0:
            print(f"You're right! Current score: {score}")
        
        correct=compare()
        score+=1

    clear()
    print(f"Sorry, that's wrong. Final score: {score-1}")
    if input("Do you want to play again? Type 'y' or 'n': ").lower()=="y":
        game()

game()
    


    