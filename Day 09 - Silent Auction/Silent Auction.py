import art
import os

def clear():
    os.system('cls')

#HINT: You can call clear() to clear the output in the console.

bids={}
bidding="yes"
highest_bid=0

while bidding=="yes":
  print(art.logo)
  name=input("What's your name? ")
  bid=float(input("What's your bid? $"))
  bids[name]=bid
  bidding=input("Are there any other bidders? Type 'yes' or 'no' ").lower

for bidder in bids:
  if bids[bidder]>highest_bid:
    winner=bidder
    highest_bid=bids[bidder]

print(art.logo)
print(f"The winner is {winner} with a bid of ${highest_bid}")