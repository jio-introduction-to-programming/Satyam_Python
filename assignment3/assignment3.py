#############################################################
# Q1.
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num % 2 == 0:
        break
    print(num)
else:
    print("All numbers are even")

# Ans. 1
# 1

#############################################################
# Q2.
i = 0
while i < 5:
    if i == 3:
        break
    i += 1
print(i)

# Ans. 2.
# 3

#############################################################
# Q3.
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i, end=' ')
else:
    if i == 5:
        print("Loop completed successfully", end=' ')

# Ans. 3
# 1 2 4 5 Loop completed successfully

#############################################################
# Q4.
i = 0 
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i, end=' ')

# Ans. 4
# 1 2 4 5 

#############################################################
# Q5.
numbers = [1, 2, 3, 4, 5]
total = 0
for num in numbers:
    if num == 3:
        break
    total += num
print(total)

# Ans. 5
# 3

#############################################################
# Q6.
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num % 2 == 0:
        continue
    print(num)

# Ans. 6
# 1
# 3
# 5

#############################################################
# Q7.
numbers = [1, 2, 3, 4, 5]
total = 0
for num in numbers:
    if num % 2 != 0:
        total += num
print(total)

# Ans. 7
# 9

#############################################################
# Q8.
x = 10
y = 5
if x > y:
    print("x is greater than y")
elif x == y:
    print("x is equal to y")
else:
    print("x is less than y")

# Ans. 8
# x is greater than y

#############################################################
# Q9.
x = 5
y = 3
if x > y:
    if x % y == 0:
        print("x is divisible by y")
    else:
        print("x is not divisible by y")
else:
    print("Invalid comparison")

# Ans. 9
# x is not divisible by y

#############################################################
# Q10.
x = 100
while x > 0:
    print(x, end=' ')
    x = x // 2

# Ans. 10
# 100 50 25 12 6 3 1 

#############################################################
