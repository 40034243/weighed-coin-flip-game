from decimal import Decimal
import random
loss_rate = 0
count = 0
total = 0

betting_amount = 100
amount_of_rounds_tested = 365

for i in range(amount_of_rounds_tested):
    new_balance = 100
    flips = 0
    while flips < 100000:
        if random.randint(0, 100) <= 51:
            new_balance = Decimal(Decimal(new_balance) + Decimal(betting_amount))
        else:
            new_balance = Decimal(Decimal(new_balance) - Decimal(betting_amount))
        
        if new_balance <= 0:
            break
        flips += 1
        
    print(new_balance)
    
    if new_balance < 100:
        loss_rate += 1
        

print(new_balance)
print("Loss rate:", loss_rate / amount_of_rounds_tested * 100,"%")
        

    
    
    
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
    
    


    
