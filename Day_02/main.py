# Understanding data types and how to manipulate strings

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

# Different solution
# tip_as_percentage =  tip / 100
# total_tip_amount = bill * tip_as_percentage
# total_bill = bill + total_tip_amount
# bill_per_person = total_bill / people
# total = round(bill_per_person, 2)
# print(f"Each person should pay £{total}")

# My solution
tip_percentage =  tip / 100
individual_total = bill / people
individual_tip = individual_total * tip_percentage
total = (bill / people) + individual_tip

print(f"Each person should pay: £{total:.2f}") #:.2f gives two decimal places even when there is a zero