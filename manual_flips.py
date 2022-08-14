from decimal import Decimal
import random


balance = 100


for i in range(1):
    print("Please input H or T: ")
    x = input()
    print("Please input bet amount: ")
    y = input()
    if x == "H":
        if random.randint(0, 100) <= 60:
            print("You won!")
            new_balance = Decimal(Decimal(balance) + Decimal(y))
            print("New Balance: ")
            print(new_balance)
        else:
            print("You lost.")
            new_balance = Decimal(Decimal(balance) - Decimal(y))
            print("New Balance: ")
            print(new_balance)
            
    else:
        print("You lost.")
        new_balance = Decimal(Decimal(balance) - Decimal(y))
        print("New Balance: ")
        print(new_balance)
        
    if balance <= 0:
            exit()
            
    while True:
        print("Please input H or T: ")
        x = input()
        print("Please input bet amount: ")
        y = input()
        if x == "H":
            if random.randint(0, 100) <= 60:
                print("You won!")
                new_balance = Decimal(Decimal(new_balance) + Decimal(y))
                print("New Balance: ")
                print(new_balance)
            else:
                print("You lost.")
                new_balance = Decimal(Decimal(new_balance) - Decimal(y))
                print("New Balance: ")
                print(new_balance)
                
        if x == "T":
            if random.randint(0, 100) <= 40:
                print("You won!")
                new_balance = Decimal(Decimal(new_balance) + Decimal(y))
                print("New Balance: ")
                print(new_balance)
            else:
                print("You lost.")
                new_balance = Decimal(Decimal(new_balance) - Decimal(y))
                print("New Balance: ")
                print(new_balance)
                
        if new_balance <= 0:
            exit()
            
            
