import os
import random
from art import logo

cards=["A",2,3,4,5,6,7,8,9,10,"J","Q","K"]

def clear():
    os.system('cls')

def deal(hand,deck):
    """Deals a random card to a player and removes it from the deck"""
    card=random.choice(deck)
    hand.append(card)
    deck.remove(card)

def calculate_value(hand):
    """Calculates the total value of a player's hand"""
    aces=0
    total=0
    for card in hand:
        if isinstance(card,int):
            total+=card
        elif card != "A":
            total+=10
        else:
            aces+=1

        for i in range(aces):
            if total+11*aces>21:
                total+=1
                aces-=1
            else:
                total+=11
                aces-=1
    
    return total

def bust_or_21(total, player, player_hand,player_score,dealer_hand,dealer_score):
    if total > 21:
        print(f"Your final hand is: {player_hand}, your final score is {player_score}")
        print(f"The dealer's final hand is: {dealer_hand}, their final score is {dealer_score}")
        
        if player=="player":
            print("You have gone over 21, the dealer wins!")
        else:
            print("The dealer has gone over 21, you win!")
        
        return True
    elif total == 21:
        print(f"Your final hand is: {player_hand}, your final score is {player_score}")
        print(f"The dealer's final hand is: {dealer_hand}, their final score is {dealer_score}")
        if player=="player":
            print("You have exactly 21, you win!")
        else:
            print("The dealer has exactly 21, the dealer wins!")
        
        return True
    else:
        return False

def blackjack(cards=cards):
    clear()
    print(logo)
    deck=4*cards

    player=[]

    dealer=[]

    deal(player,deck)
    player_score=calculate_value(player)

    deal(dealer,deck)
    deal(dealer,deck)
    dealer_score=calculate_value(dealer)

    game_over=False

    while not game_over:
        deal(player,deck)
        player_score=calculate_value(player)
        print(f"Your cards are: {player}, current score: {player_score} ")
        game_over=bust_or_21(player_score,"player",player,player_score,dealer,dealer_score)
        at_least_21=game_over

        if not game_over:
            if input("type 'y' to get another card, type 'n' to pass\n")!="y":
                game_over=True

    if not at_least_21:

        while dealer_score < 17:
            deal(dealer,deck)
            dealer_score=calculate_value(dealer)
    
        at_least_21=bust_or_21(dealer_score,"dealer",player,player_score,dealer,dealer_score)

        if not at_least_21:
            print(f"Your final hand is: {player}, your final score is {player_score}")
            print(f"The dealer's final hand is: {dealer}, their final score is {dealer_score}")

            if player_score<dealer_score:
                print("The dealer's score is higher, the dealer wins!")
            elif player_score>dealer_score:
                print("Your score is higher, you win!")
            else:
                print("Both scores are equal. It's a draw")


    if input("Do you want to play another round? Type 'y' to play again\n")=="y":
        blackjack()

clear()
print(logo)
if input("Do you want to play a friendly game of blackjack? Type 'y' to start a game\n")=="y":
    blackjack()



