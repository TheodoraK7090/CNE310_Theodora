def howManyMonths(start, rate, spending, target):
    
    
    months = 0
    balance = start

    while True:
        months+=1
    
        balance = balance * (1 + rate) - spending

        if balance >= target:
            return months

        if balance < 0:
            return -1

        if months == 100:
            return -1

print(howManyMonths(15000, 0.03, 100, 20000))