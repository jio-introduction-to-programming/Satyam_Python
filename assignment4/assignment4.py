'''
1. Write a function which takes a list as input and return its sum1.
2. Write a function which takes a list as an input and return the max element in the list 
3. Write a function which takes a list as input and returns the reverse of the list in the output
4. Write a function which takes a list asinput and returns the list in sortedformat. ( Note: You're not allowed to use in-built functions ) 
    Mean / Average, Mode  
5. Write a function which takes a list asan input and returns the following statistics: 
    1. mean/average
    2. mode
6. 
Step-1 Read a sequence of numbersas an input from user. 
Step-2 Read another integer k fromthe user 
Step-3 Ask user to input two numberstart and end, k times 
Step-4 Return the sum of the arrayfrom start -> end as a result in the k-sized list 
'''

# 1. Write a function which takes a list as input and return its sum1.
def add(lst):
    return sum(lst)

print(add([1,2,3,4,5]))

# 2. Write a function which takes a list as an input and return the max element in the list 

def lst_max(lst):
    return max(lst)

print(lst_max([1,2,3,4,5]))

# 3. Write a function which takes a list as input and returns the reverse of the list in the output

def reverse_lst(lst):
    lst.reverse()
    return lst

print(reverse_lst([1,2,3,4,5]))

# 4. Write a function which takes a list as input and returns the list in sorted format. 
# (Note: You're not allowed to use in-built functions)

def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j>=0 and key<arr[j]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            j = j - 1

    return arr

insertionSort([3,2,4,1,5,3])


# 5. Write a function which takes a list as an input and returns the following statistics: 
#     1. mean/average
#     2. mode

def calc_stats(lst):
    mean = sum(lst)/len(lst)
    nums_dict = {}
    for num in lst:
        if num in nums_dict:
            nums_dict[num] += 1
        else:
            nums_dict[num] = 1
    
    mode_count = max(nums_dict.values())
    mode = [key for key in nums_dict.keys() if nums_dict[key] == mode_count]

    return f'mean is: {mean}, \nmode is: {mode}'

print(calc_stats([1,1,1,2,2,2,3,8,12]))


# 6. 
# Step-1 Read a sequence of numbers as an input from user. 
# Step-2 Read another integer k from the user 
# Step-3 Ask user to input two number start and end, k times 
# Step-4 Return the sum of the array from start -> end as a result in the k-sized list 

# arr = 1 5 -6 10 -34 19 8 6 , k = 3
arr = list(map(int, input('Enter space separated integers (minimum 5 numbers): ').split()))
k = int(input('Enter the number of times you want the sum: '))
lst = []
for i in range(k):
    indexes = list(map(int, input('Enter the start and end index values (space separated) to get the sum from the list: ').split()))
    sum_start_to_end_index = add(arr[indexes[0]: indexes[1]+1])
    lst.append(sum_start_to_end_index)
print(lst)

