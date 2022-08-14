from decimal import Decimal

import random

loss_rate = 0
count = 0
total = 0

new_balance = 100
betting_amount = new_balance * .10000000000000009
amount_of_rounds_tested = 1

for i in range(amount_of_rounds_tested):
    new_balance = 100
    flips = 0
    while flips < 100000:
        if random.randint(0, 100) <= 55:
            new_balance = Decimal(Decimal(new_balance) + Decimal(betting_amount))
        else:
            new_balance = Decimal(Decimal(new_balance) - Decimal(betting_amount))
        
        flips += 1
        if new_balance <= 0:
            break
        
    print(new_balance)
    
    if new_balance < 100:
        loss_rate += 1

print("Loss rate:", loss_rate / amount_of_rounds_tested * 100,"%")
    
