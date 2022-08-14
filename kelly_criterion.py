b = 1 #payout
p = 0.55 #odds of winning /1

kelly = ((p * b - (1 - p))/b) * 100

print(kelly)
