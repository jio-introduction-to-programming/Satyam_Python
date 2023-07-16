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

y = 1.0
formatted = f'{y:.2f}'
print(formatted)

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

numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num % 2 == 0:
        break
    print(num)
else:
    print("All numbers are even")

##########################################################

lst = []
lst_all_dtypes = [1, 'a', 0.33]
lst_all_dtypes

grid = [[0, 1, 0],
        [1, 1, 0],
        [0, 0, 1]]

grid

odds = [x for x in range(1,10,2)]
odds

print(*[x for x in range(0,10) if x%2 == 0])

a = [[0]*5]*5
a[0][0] = 2
a

import random

[random.randint(1,100) for _ in range(5)]

[random.random() for _ in range(2)]

lst_sample = random.sample(range(1,100), 5)
lst_sample

my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list)
my_list

del my_list[2]
my_list
my_list[-4]
# list slicing mylist[start:stop:step]
new_list = my_list[0:4:2]
# new_list.clear()
new_list

c = my_list.pop()
c

id(my_list[0]) == id(new_list[0])
my_list.index(10)
my_list.pop(-1)

dict_a = {True: a}
dict_a
dir(dict_a)

keys = ['a', 'b', 'c']
my_dict = {k:v for k,v in enumerate(keys)}
my_dict
default_price = 0.99
eg_dict = dict.fromkeys(keys, default_price)
eg_dict
price_list = [1, 3, 5]
eg2_dict = dict.fromkeys(keys, price_list) # cannot pass a list of values, other
eg2_dict

print(my_dict.get('d', 'default'))

my_dict.items() # returns a list - items(), keys(), values()

{}.pop('key','a')

a_dict = {1 : 'a',
          2 : 'b'}

b_dict = dict(a_dict)
b_dict
last_inserted_item = b_dict.popitem()
last_inserted_item

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

g = []
h = []
id(g) == id(h)

a = [1,2,3]
b = a[:]

print(id(a), id(b), sep='\n')

b[0] = 4

a[1] = 5

print(a, b, sep='\n')

id(a[1]) == id(b[1])

import copy

orig_list = [1, 2, 3, 4]
new_list = copy.deepcopy(orig_list)

id(orig_list[1]) == id(new_list[1])
