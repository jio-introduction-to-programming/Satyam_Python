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

print(1e2 == 100.0)
print(1e-2 == 0.01)

type(format(11))

x = 3.141516
formatted = '{:.2f}'.format(x)
print(formatted)

# formatted = f'{.2f}'
# print(formatted)

birthdate = input("Enter your upcoming birthdate in dd/mm/yyyy format: ")
birthdate = datetime.strptime(birthdate, '%d/%m/%y')

todays_date = datetime.date.today()

delta = datetime.timedelta(birthdate,todays_date)

#############################################################################################

n = 3

print('Even' if n%2==0 else 'Odd')

def show_grade(score):
    if score>=80:
        grade = 'A'
    elif score >= 60:
        grade = 'B'
    elif score >= 40:
        grade = 'C'
    else:
        grade = 'D'
    return grade

score = int(input("Enter the score: "))
grade = show_grade(score)
print('Your grade is',grade)

'a'.isalpha() #True
'ab'.isalpha() #True
'5'.isalpha() #False
'@'.isalpha() #False
'1'.isdigit()
'a'.isupper()
'A'.islower()

import time

# countdown
def blastoff(count):
    while count>0:
        print(count, end=' ')
        count-=1
        time.sleep(1) # Adds a delay of 1 second
    return "\nBlastoff!"

count = 5
print(blastoff(count))


# table
def tables(m,n):
    for i in range(1,n+1):
        print(m*i, end=' ')

m=5
n=15
tables(m,n)

#############
print([char for char in 'Satyam'])

fruits = ['apple', 'banana', 'orange']

for index, fruit in enumerate(fruits):
    print(f"Index: {index}, Fruit: {fruit}")

search_fruit = 'kiwi'

print("Found Fruit" if search_fruit in fruits else "Fruit not Found")

numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num%2 == 0:
        continue
    print(num)

