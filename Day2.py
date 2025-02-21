print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = float(input("What percentage tip would you like to give?"))
people = int(input("How many people to split the bill? "))
total_tip=(tip/100)*bill
print(f'your tip:${round(total_tip,2)}')
total_bill=bill+total_tip
print(f'your total bill:${round(total_bill,2)}')
people_share=total_bill/people
print(f'your bill share per person:${round(people_share,2)}')