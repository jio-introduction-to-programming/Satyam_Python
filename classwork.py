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

type(set({'a':1}))

print(set({'a':1}))

set([1,2,3,2])

vegetables = {'tomato', 'carrot', 'radish', 'brinjal'}
vegetables.add('pumpkin')
vegetables.clear()
vegetables

vegetables = {'tomato', 'carrot', 'radish', 'brinjal'}
veg_copy = vegetables.copy() # Creates a shallow copy
veg_copy

a = {1,2,3,4,5}
b = {4, 5, 6, 7} 
c = a-b # a - b or a.difference(b)

a.difference_update(b)
a 

x = vegetables.discard('ladyfinger')
x = vegetables.discard('radish')
vegetables

a = {1,2,3,4,5}
b = {4, 5, 6, 7} 
a.intersection_update(b)
a

a = {1,2,3}
b = {3,4,5}
c = {6,7,8}
a.isdisjoint(b)
a.isdisjoint(c)

d = {1,2}
d.issubset(b)
d.issubset(a)

a.issuperset(d)

a = {2,3,4,1,5,6,7,8,9,10}
b = a.pop()
a
b
a.remove(10)
a
a.remove(11) # keyerror
a.discard(11) # None - no error

a = {1,2,3}
b = {3,4,5}
a.symmetric_difference(b)
a.symmetric_difference_update(b)
a

a.union(b)
a

a.update(b)
a
##############################################
t = tuple()
t
type(t)

u = ()
u
type(u)

# Parenthesis Overloading Problem

a = (1)
type(a)

b = (True)
type(b)

c = ('first')
type(c)

d = (1,)
type(d)

e = (1, 1)
type(e)

# tuple operations: indexing, slicing, iterating

# tuple methods: .count(num), .index(num)

def sum_of_list(lst):
    return sum(lst)

a_lst = [1, 2, 3]
print(sum_of_list(a_lst))

print((1,2,3)*2)
print((1,2,3)+(4,))

##########################################################

# Recursion

def factorial(n):
    # base case: factorial or 0 and 1 is 1
    if n==0 or n==1:
        return 1
    else:
        # Recursive case: multiply n with factorial of (n-1)
        return n*factorial(n-1)

factorial(5)

# Unpacking

# args
def func(a, b, c):
    print(a, b, c)

args = [1,2,3]
func(*args)

# keyword args
def func(**kwargs):
    for key, value in kwargs.items():
        print(key, value)

func(key=1, value=2)

def count_vowels(string):
    vowels = 'aeiouAEIOU'
    counter = 0
    for char in string:
        if char in vowels:
            counter += 1

    return counter

string = 'Hello wOrld!'
print(count_vowels(string))

####################

# string methods

# string.capitalize() --> it capitalize the first letter of a sentence and everything else in lowercase
print(string.capitalize(), string)

# string.casefold() --> returns a lowercase version of the string, suitable for case-insensitive comparision
# string.center(width [,filler])
string = 'hello'
centered_string = string.center(10, '-')
print(centered_string)

print(centered_string.center(10)) # default is ' ' (space)

# count(substring [, start [,end]]) --> returns the number of non-overlapping occurances of a substring in a string

string = 'hello world'
count = string.count('o')
print(count)

# string.endswith(substr) --> returns True or False
# string.startsswith(substr) --> returns True or False
# string.find(sub [, start [, end]]) --> returns the index of first 
# string.isalnum(), isalpha(), isdecimal(), isdigit(), islower(), isspace()
# ''.join(list or iterable), string.lower(), string.split(''), string.swapcase()
# string.strip(char) --> removes the leading and trailing characters provided
# isascii() --> checks if string consists only of ASCII characters

print('123'.isdecimal()) # True
print('123.11'.isdecimal()) # False
print('X'.isdecimal()) # False
print('123'.isdigit()) # True
print('  '.isspace()) # True
print(' '.join('hello'))
print('###abc## '.strip('#'))
##########################

# format(*args, **kwargs)

# format_map(dict) --> maps the keys, values from a dictionary to string.format_map()

##########################
print('abc'[::-1])
##############################################################################

### OOP - Object Oriented Programming ###

class Car:
    name = None
    color = None

car1 = Car()
car1.name = "Maruti"
car1.color = "White"
print(car1.name)
print(car1.color)

#####################################

# Constructor of class in Python

class Car:
     
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.state = 'OFF'
    
    def start(self):
        self.state = 'ON'


maruti = Car('m-800', 'blue')
maruti.start()
maruti.color
print(maruti.state)

thar = Car('XUV-300', 'white')
# thar.start()
print(thar.state)

#######################################

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I'm {self.age} years old.")

person1 = Person('John', 26)
print(person1.age)
person1.greet()

#######################################

class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

    def set_next(self, next):
        self.next = next


node1 = Node(2)
node2 = Node(4)
print(type(node2))
node1.set_next(id(node2))
node3 = Node(6)
node2.set_next(node3)
print(node1.next)

#######################################

## Inheritence ##

class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    def calculate_salary(self):
        print("Calculating salary:...")

class Manager(Employee):
    def __init__(self, name, employee_id):
        super().__init__(name, employee_id)

    def approve_leave(self):
        print("Approving leave...")

class Engineer(Employee):
    def __init__(self, name, employee_id):
        super().__init__(name, employee_id)

###############################################

# __dunder_method__: these are often referred to as 'magic' or 'dunder' (double underscore) method
### we can have multi-level inheritence

class Furniture:
    def __init__(self, material):
        self.material = material

    def sit(self):
        print('Sitting...')

###############################################

# Lambda functions

square = lambda x: x**2
square(2)

# map(function, iterable) # can be any function /lambda, inbuilt, etc.
# filter(function, iterable) # any function that evaluates to boolean.


# cumulative sum array or prefix sum array

#################################################################################################

# 24-07-2023

### File Operations ###

# Open the file with write 'w' mode
file1 = open('example.txt', 'w')

# write some data to the file
file1.write('Persisting data in files using Python')

# close the file
file1.close()

import io
# Read the file
img_file = io.open('C:\\Users\\Richa\\Downloads\\Zoom-Meeting-Video-Iphone-Portrait-Mode-Background.jpeg', encoding="utf8")
print(img_file.read())

file1_read = open('example.txt', 'r')
file1_read.read()
file1_read.close()

import os

os.remove('example.txt')

# to overwrite, simply do the write operation to the file

# Appending to a file

file = open('example.txt', 'a')

# write some data to the file
file.write('\nAppending data in files using Python')

# close the file
file1.close()

### Binary files in python
bin_file = open('binary_file.bin', 'wb')

# bin_file.write(b'Writing to the binary file')
bin_file.write(b'[0,1,2,3,4]')

bin_file.close()

list('[0,1,2,3,4]') #['[', '0', ',', '1', ',', '2', ',', '3', ',', '4', ']']
eval('[0,1,2,3,4]')

## reading an image file

# import cv2

# load image using 'imread'
# img = 

import pickle
data = {'key': 'value'}


import json

import sys
sys.version


#################################################################################################

from datetime import datetime, date

def datetime_to_str_1(dt):
    # Convert to format "2023-07-19"
    form_date = dt.strftime('%Y-%m-%d')
    return form_date

print(datetime_to_str_1(date(2023,7,24)))

print(date(2023, 7, 19))

print([5*x for x in range(1, 21)])

#################################################################################################

### Function closure concept ###

def create_num_list(num):
    def multiply_by(n):
        return list(map(lambda i: n*i, range(1, num+1)))
    return multiply_by

multiplier = create_num_list(20)
print(multiplier(5))
print(multiplier(7))

#################################################################################################

import sys

sys.getsizeof(1) # 28
sys.getsizeof(111) # 28

sys.getsizeof('') # 49
sys.getsizeof('a') # 50
sys.getsizeof('ab') # 51

sys.getsizeof(True) # 28
sys.getsizeof(False) # 28

sys.getsizeof(1.1) # 24

dir(1) 
'''
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', 
'__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__',
 '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__getstate__', '__gt__',
   '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', 
   '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__',
     '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__',
       '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__',
         '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__',
           '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', 
           '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 
           'bit_count', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag',
             'numerator', 'real', 'to_bytes']
'''
type(1) #<class 'int'>

##################################################################################

### Debugging the Python Code - Python Debugger (pdb)

import pdb

def abc():
    print(1)
    pdb.set_trace()
    print(2)
    print(3)
    print(4)

abc()

# type n in the python shell to go to next line one line at a time.
# type c to exit debugger mode and continue further code at once

##################################################################################

# checking dependencies

# pip freeze --> to check all the dependencies to be installed when sending our package to other place
# pip freeze > requirements.txt --> to get them into a file

# pip install -r requirements.txt --> to install all dependencies at once reading from the file

##################################################################################

def fact(n):
    if n in [0, 1] :
        return 1
    elif n > 1:
        return n*fact(n-1)
    else:
        return 'not possible'
    
print((fact(5)))


(4**0.5)-int(4**0.5) == 0

import sys
print (sys.version)

set([1, 1, (3,4), (3,4)])

eval('')