from art import logo
import random
import os

def clear ():
    os.system("cls")

def play():

    clear()
    print(logo)
    number=random.randint(1,100)

    difficulty=input("\nI'm thinking of a number between 1 and 100. \nChoose a dificulty. Type 'easy' or 'hard': ").lower()
    if difficulty=="easy":
        attempts=10
    else:
        attempts=5

    while attempts>0:    
        print(f"\nYou have {attempts} attempts remaining to guess the number")
        guess=int(input("Make a guess: "))

        if guess > number:
            print("Too high. \nGuess again.")
            attempts-=1
        elif guess < number:
            print("Too low. \nGuess again.")
            attempts-=1
        else:
            print(f"\nYou got it! The answer was {guess}")
            break

    if attempts==0:
        print("\nYou've run out of guesses. You lose")           

    if input("\nDo you want to play again? Type 'yes' or 'no': ").lower()=='yes':
        play()

play()


