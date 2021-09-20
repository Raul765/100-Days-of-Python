#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python
print("Welcome to the tip calculator")
total_bill=float(input("What was the total of the bill? $"))
percentage_tip=float(input("What percentage tip would you like to give? "))
number_of_people=int(input("How many people to split the bill? "))

amount_per_person=round(((total_bill*(1+(percentage_tip/100)))/number_of_people),2)

amount_per_person="{:.2f}".format(amount_per_person)

print("Each person should pay $" +amount_per_person)