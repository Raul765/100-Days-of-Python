from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu=Menu()
money_machine=MoneyMachine()
coffee_maker=CoffeeMaker()

def machine():
    item=False

    order=input("What would you like? (espresso/latte/cappuccino/):​ ")
    if order=="off":
        return
    elif order=="report":
        coffee_maker.report()
        money_machine.report()
    else:
        item=menu.find_drink(order)
    
    if item!=False:
      can_make=coffee_maker.is_resource_sufficient(item)  

      if can_make:
          can_pay=money_machine.make_payment(item.cost)

          if can_pay:
              coffee_maker.make_coffee(item)

    machine()

machine()

