# 1. importing the whole module
import calculator
print(calculator.add(10,5))

# 2. importing specific functions from the module
from calculator import multiply
print(multiply(10,5))

# 3. Alias
import calculator as cal
print(cal.add(20,30,))

# build-in modules
import math
import random

print(math.sqrt(16)) # 4.0
print(random.randint(1,6)) # random integer between 1 and 6 (inclusive)