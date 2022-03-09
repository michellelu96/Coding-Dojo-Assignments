#Countdown


from array import array
from hashlib import new


def countdown(count):
    array=[]
    for x in range(count,-1,-1):
        array.append(x)
    return array

print(countdown(5))

#print and return

def print_and_return(arr):
    print(arr[0])
    return arr[1]

print(print_and_return([1,2]))

#first plus length
def first_plus_length(arr):
    a = arr[0]
    b= len(arr)
    return a+b

print(first_plus_length([1,2,3,4,5]))

#values greater than second

def values_greater_than_second(arr):
    newarr=[]
    if len(arr) <= 2:
        return False
    for x in range(0,len(arr),1):
        if arr[x] > arr[1]:
            newarr.append(arr[x])
    return newarr
    
print(values_greater_than_second([5,2,3,2,1,4]))
print(values_greater_than_second([3]))

#this length,that value
def length_and_value(l,v):
    newarr=[]
    for x in range(l):
        newarr.append(v)
    return newarr

print(length_and_value(4,7))
print(length_and_value(6,2))