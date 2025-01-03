# Understanding data types and how to manipulate strings

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

tip_percentage =  tip / 100
individual_total = bill / people
individual_tip = individual_total * tip_percentage
total = (bill / people) + individual_tip

print(f"Each person should pay: £{total:.2f}") #:.2f gives two decimal places even when there is a zero