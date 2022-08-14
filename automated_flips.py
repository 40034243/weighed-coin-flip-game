from decimal import Decimal
import random

total = 0

betting_amount = 20

while True:
        new_balance = 100
        flips = 0
        while flips < 1000:
            if random.randint(0, 100) <= 60:
                new_balance = Decimal(Decimal(new_balance) + Decimal(betting_amount))
            else:
                new_balance = Decimal(Decimal(new_balance) - Decimal(betting_amount))
            
            flips += 1
            
            if new_balance <= 0:
                print("BANKRUPT! after", flips, "flips")
                bankruptcy_rate = 1 / (total + 1) * 100
                print("Bankruptcy rate:", bankruptcy_rate, "%")
                exit()
            
        total += 1     
        print(new_balance)
