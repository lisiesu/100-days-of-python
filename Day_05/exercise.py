# FizzBuzz in Python

# The program should print each number from 1 to 100
# When the number is divisible by 3, instead of printing the number, print "Fizz"
# When the number is divisible by 5, instead of printing the number, print "Buzz"
# When the number is divisible by both 3 and 5, instead of printing the number, print "FizzBuzz"

for number in range(1, 101):
    if number % 3 == 0 and number % 5== 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print (number)
