# Initial investment
p = 1000 
r = 0.07  

# Years to calculate for
years = [10, 20, 30]

# Calculate and display results
print("Year\tAmount on Deposit")
for n in years:
    a = p * (1 + r) ** n
    print(f"{n}\t${a:.2f}")
