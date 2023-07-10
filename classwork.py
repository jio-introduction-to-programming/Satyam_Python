import datetime
current_time = datetime.datetime.now()
print(current_time)

import time
start_time = time.time()
print(start_time)
end_time = time.time()
print(end_time)
running_time = end_time - start_time
print(running_time)

import math

math.sqrt(200)
math.ceil(3.7)
math.factorial(5)

dir(math)

import random

random_float = random.uniform(0.5, 1.5)
print(random_float)

random_number = random.random()
print(random_number)

all([True, 1, {}, 'Hello']) 

all([1==0])

ord('A')

chr(97)