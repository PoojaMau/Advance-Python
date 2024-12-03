# Simple interest Calculation

def simple_interest(p, n, r):
    i = (p*n*r)/100
    amt = p + i
    return {"interest": i, "amount": amt}

# Take input from user in cansole
p = float (input("Please enter principle in INR: "))
n = int (input("Please enter number of years: "))
r = float (input("Please enter rate of interest in %p.a.: "))

# Calculate interest and amount
results  = simple_interest(p, n, r)

# print the results
print(results)