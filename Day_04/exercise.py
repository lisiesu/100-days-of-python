# Write a program that randomly picks a name from a list

import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
random_number = random.randint(0, 4)
print(friends[random_number])

# Or use method:
print(random.choice(friends))
