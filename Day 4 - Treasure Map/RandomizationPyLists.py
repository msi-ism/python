import random
import my_module

random_integer = random.randint(1, 10)
print(random_integer)

print(my_module.pi)
# By multiplying random float by 5 rand becomes 0-5 not including by instead of 0-1
random_float = random.random()
print(random_float)

love_score = random.randint(1, 100)
print(f"Your love score is {love_score}.")