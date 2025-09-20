while (True):
    invAmt= float(input("Enter the investment ammount (greater than 0 less than 50000):"))
    if(invAmt > 0 and invAmt < 50000):
        break
    else:
        print("ERROR: Number is not between 0 and 50000\n")


while (True):
    invRate= float(input("Enter the interest rate (greater than 0 less than 15):"))
    if(invRate > 0 and invRate < 15):
        break
    else:
        print("ERROR: Number is not between 0 and 15\n")


while (True):
    dur= int(input("Enter the interest duration (greater than 0):"))
    if(dur > 0):
        break
    else:
        print("ERROR: Number is not greater than 0\n")


invRate /= 12.0
invRate /= 100.0
months = dur * 12
total = 0


for num in range(0, months):
    total += invAmt
    total = total * (1 + invRate)
    if ((num + 1) % 12 == 0):
        print(f"Year {num + 1 // 12}: {total:,.2f}")
   
print(f"\nInvestment duration: {dur} years")
print(f"Yearly interest rate: {invRate * 1200}%")
print(f"Monthly investment ammount: ${invAmt}")
print(f"Total ammount of investment after compounding: ${total:,.2f}")
